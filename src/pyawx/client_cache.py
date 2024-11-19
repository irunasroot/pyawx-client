__all__ = ["get_client", "set_client"]

# Stores an initialized client
CLIENT = None


def get_client():
    """
    Retrieve initialized `class:pyawx.client.Client` object.

    :rtype: `class:pyawx.client.Client`
    """
    global CLIENT
    return CLIENT


def set_client(client):
    """
    Store initialed `class:pyawx.client.Client` object.

    :type client: `class:pyawx.client.Client`
    :rtype: `class:pyawx.client.Client`
    """
    global CLIENT
    CLIENT = client
    return client
