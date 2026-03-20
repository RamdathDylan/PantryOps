from src.db.db_utils import *

def get_all_items():
    """
    Queries the database and returns every record 
    in the items table with their information. 

    Ordered by id number. 

    Returns:
    List of tuples.
    """

    sql = """
    SELECT id, name, category, unit, description 
    FROM items
    ORDER BY id
    """

    return exec_get_all(sql)

def get_item(item_id):
    """
    Queries the database and returns the record with the matching 
    id number in the items table.

    Keyword Arguments:
    id - The id of the item that is being queried.

    Return:
    Tuple or none if record not found.
    """

    sql = """
    SELECT id, name, category, unit, description
    FROM items
    WHERE id=%s
    """

    return exec_get_one(sql, (item_id,))


def get_item_by_name(name):
    """
    Queries the database and returns the record with the matching 
    name in the items table.

    Keyword Arguments:
    name - The name of the item that is being queried.

    Return:
    Tuple or none if record not found.
    """

    sql = """
    SELECT id, name, category, unit, description
    FROM items
    WHERE name=%s
    """

    return exec_get_one(sql, (name,))
