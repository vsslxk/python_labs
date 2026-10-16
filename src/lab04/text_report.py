from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

# чтобы работали импорты "from lib.text import ..." при запуске из корня репозитория
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n  # из ЛР3
from io_txt_csv import read_text, write_csv


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Возвращает все пары (слово, число) в нужном порядке.

    Порядок: count по убыванию, при равенстве слово по возрастанию.

    Args:
        freq: словарь {слово: частота}.
    """
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def load_tokens(path: str | Path, encoding: str = "utf-8") -> list[str]:
    """Читает файл и превращает его текст в список слов.

    Ошибки чтения (FileNotFoundError, UnicodeDecodeError) не перехватываются.

    Args:
        path: путь к текстовому файлу.
        encoding: кодировка файла.

    Returns:
        Список слов после нормализации и токенизации.
    """
    return tokenize(normalize(read_text(path, encoding=encoding)))


def print_table(
    rows: Sequence[tuple[str, int]],
    header: tuple[str, str] = ("word", "count"),
) -> None:
    """Печатает таблицу в консоль, ширина столбцов по самому длинному значению (★).

    Args:
        rows: пары (слово, число).
        header: заголовки двух столбцов.
    """
    data = [header] + [(word, str(count)) for word, count in rows]
    width_word = max(len(row[0]) for row in data)
    width_count = max(len(row[1]) for row in data)
    for i, (word, count) in enumerate(data):
        print(f"{word:<{width_word}} | {count:<{width_count}}")
        if i == 0:
            print("-" * width_word + "-+-" + "-" * width_count)


def parse_args() -> argparse.Namespace:
    """Разбирает параметры командной строки."""
    parser = argparse.ArgumentParser(description="Отчёт по частотам слов в текстовых файлах")
    parser.add_argument("--in", dest="inputs", nargs="+", default=["data/lab04/input.txt"],
                        help="один или несколько входных файлов")
    parser.add_argument("--out", default="data/lab04/report.csv",
                        help="выходной CSV word,count")
    parser.add_argument("--encoding", default="utf-8",
                        help="кодировка входных файлов (например cp1251)")
    parser.add_argument("--per-file", default=None,
                        help="★ CSV file,word,count по каждому файлу")
    parser.add_argument("--total", default=None,
                        help="★ сводный CSV word,count по всем файлам")
    return parser.parse_args()


def main() -> None:
    """Читает файлы, считает частоты, пишет CSV-отчёты и печатает резюме."""
    args = parse_args()

    all_tokens: list[str] = []
    per_file_rows: list[tuple[str, str, int]] = []

    for path in args.inputs:
        try:
            tokens = load_tokens(path, encoding=args.encoding)
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {path}")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Ошибка: не удалось прочитать {path} в кодировке {args.encoding}. "
                  f"Попробуйте указать другую, например --encoding cp1251")
            sys.exit(1)

        all_tokens.extend(tokens)

        freq_file = count_freq(tokens)
        name = Path(path).name
        for word, count in sorted_word_counts(freq_file):
            per_file_rows.append((name, word, count))

    freq = count_freq(all_tokens)
    rows = sorted_word_counts(freq)

    # базовый отчёт (при одном входном файле это отчёт по нему)
    write_csv(rows, args.out, header=("word", "count"))

    # ★ отчёт по каждому файлу: file ↑, count ↓, word ↑
    if args.per_file:
        per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))
        write_csv(per_file_rows, args.per_file, header=("file", "word", "count"))

    # ★ сводный отчёт по всем файлам
    if args.total:
        write_csv(rows, args.total, header=("word", "count"))

    print(f"Всего слов: {len(all_tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")

    print()
    print_table(rows)


if __name__ == "__main__":
    main()