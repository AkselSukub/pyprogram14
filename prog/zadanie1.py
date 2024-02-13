#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def collection_converter(type):
    def convert_to_collection(numbers):
        if type == 'list':
            collection = list(map(int, numbers.split()))
        else:
            collection = tuple(map(int, numbers.split()))
        return collection

    return convert_to_collection


type_input = input("Введите тип коллекции ('list' или 'tuple'): ")
numbers_input = input("Введите список целых чисел, записанных через пробел: ")

if __name__ == "__main__":
    converter = collection_converter(type_input)
    result = converter(numbers_input)
    print(result)
