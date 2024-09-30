from app import db


def add_record(record):
    """
    Add a record to the database and commit the session.

    Args:
        record: The record object to add (e.g., a User or Transaction).
    """
    db.session.add(record)
    update_record()


def delete_record(record):
    """
    Delete a record from the database and commit the session.

    Args:
        record: The record object to delete (e.g., a User or Transaction).
    """
    db.session.delete(record)
    update_record()


def find_record_by_id(model, record_id):
    """
    Find a single record by its ID.

    Args:
        model: The model class (e.g., User, Account).
        record_id: The ID of the record to find.

    Returns:
        The found record or None if not found.
    """
    return model.query.get(record_id)


def find_records_by_filter(model, **filters):
    """
    Find records that match given filter criteria.

    Args:
        model: The model class (e.g., User, Account).
        filters: Arbitrary keyword arguments to filter by (e.g., username='john').

    Returns:
        A list of matching records.
    """
    return model.query.filter_by(**filters).all()


def update_record():
    """
    Commit changes to an existing record in the database.
    """
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
