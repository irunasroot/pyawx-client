def delete(model):
    """
    Marks a record as deleted

    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :return: model
    """

    model.__delete_record__()
    return model


def export(model):
    """
    Exports the data from a model as a dict
    :param model: The model
    :type model: subclass of :class:`pyawx.models.mixins.DataModelMixin`
    :return: dict
    """
    model.__export__()
