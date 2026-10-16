from __future__ import annotations
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Функция принимает файл и необходимую кодировку(базово - "utf-8", другую необходимо явно указать)
    Возвращает содержимое файла как строку
    Если файл не найден - ошибка FileNotFoundError
    Если кодировка не подходит - ошибка UnicodeDecodeError
    '''
    file = Path(path)
    return file.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создает родительские директории для path, если их ещё нет
    '''
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    '''
    Функция принимает строки данных, путь к файлу, необязательный заголовок
    Возвращает измененный CSV-файл
    Разная длина строк(заголовка) - ошибка ValueError
    '''
    p = Path(path)
    rows = list(rows)
    lenghts = {len(row) for row in rows}
    if header is not None: lenghts.add(len(header))
    if len(lenghts) >= 2: raise ValueError('Строки разной длины!')
    
    ensure_parent_dir(path)
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

    