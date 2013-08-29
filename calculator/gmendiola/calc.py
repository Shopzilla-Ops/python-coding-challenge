#!/usr/bin/python2.7

import argparse


def _group_tokens(tokens):
    while '(' in tokens:
        depth = 0
        start = None
        for index, token in enumerate(tokens):
            if token == '(':
                start = index if start is None else start
                depth += 1
            elif token == ')':
                depth -= 1
                if depth == 0:
                    end = index
                    break
        else:
            raise Exception('Parentheses do not match')
        tokens = (
            tokens[:start] +
            [_group_tokens(tokens[start + 1:end])] +
            tokens[end + 1:]
        )
    return tokens


def _parse(expression):
    tokens = []
    digits = ''
    if expression.count('(') != expression.count(')'):
        raise Exception('Unequal number of parentheses')
    for index, character in enumerate(expression):
        if character.isdigit() or character == '.':
            digits = digits + character
            if index < len(expression) - 1:
                continue
        if digits:
            tokens.append(float(digits))
        if character in '()^*/+-':
            tokens.append(character)
        digits = ''
    if '(' in tokens:
        return _group_tokens(tokens)
    else:
        return tokens


def _reduce_expression(tokens):
    if isinstance(tokens, (int, float)):
        return tokens
    handlers = {
        '^': lambda l, r: l ** r,
        '*': lambda l, r: l * r,
        '/': lambda l, r: l / r,
        '+': lambda l, r: l + r,
        '-': lambda l, r: l - r,
    }
    operation_groups = ['^', '*/', '+-']
    for operation_group in operation_groups:
        for index, token in enumerate(tokens):
            if isinstance(token, basestring) and token in operation_group:
                operator_pos = index
                operator = token
                break
        else:
            continue
        break
    else:
        raise Exception('Invalid expression')
    if index == 0 or index == len(tokens) - 1:
        raise Exception('Invalid expression')
    left = tokens[operator_pos - 1]
    right = tokens[operator_pos + 1]
    result = handlers[operator](
        _reduce_expression(left),
        _reduce_expression(right))
    before = tokens[:operator_pos - 1]
    after = tokens[operator_pos + 2:] if len(tokens) > operator_pos + 1 else []
    if before or after:
        return _reduce_expression(before + [result] + after)
    else:
        return result


def calculate(expression):
    tokens = _parse(expression)
    return _reduce_expression(tokens)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Evaluate mathematical expression')
    parser.add_argument('expression', help='Expression to evaluate')
    args = parser.parse_args()
    print calculate(args.expression)
