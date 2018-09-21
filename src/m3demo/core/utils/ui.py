# coding: utf-8


def reorder_controls(controls, order):
    u"""Изменяет порядок элементов формы в соответствии с *order*.

    Функция может быть использована в т.ч. для элементов формы, созданных с
    помощью *objectpack.ui.model_fields_to_controls()*. Функция
    *model_fields_to_controls()* создает элементы в соответствии с порядком
    полей в соответствующей модели, что не всегда подходит.

    Элементы, указанные в *order* размещаются в начале списка *controls*.
    Остальные элементы списка *controls* остаются с исходном порядке.

    :param list controls: Список элементов формы.
    :param list order: Список имен полей, упорядоченный в нужной
        последовательности.

    :raises ValueError: Если в списке *order* указано имя отсутствующего в
        *controls* элемента.
    """
    controls.sort(
        key=lambda i: order.index(i.name) if i.name in order else len(order)
    )
