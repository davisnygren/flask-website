# Search functionality implemented with Elasticsearch, contained to this module
# to be easily replaceable.
# The same model ids from the app database are used for convenience.
from flask import current_app

# Add an entry to the index. Elastic search will update entries if the id
# already exists.
def add_to_index(index, model):
    # do nothing if search is disabled
    if not current_app.elasticsearch:
        return
    payload = {}
    for field in model.__searchable__:
        payload[field] = getattr(model, field)
    current_app.elasticsearch.index(index=index, id=model.id, document=payload)

def remove_from_index(index, model):
    # do nothing if search is disabled
    if not current_app.elasticsearch:
        return
    current_app.elasticsearch.delete(index=index, id=model.id)

def query_index(index, query, page, per_page):
    # do nothing if search is disabled
    if not current_app.elasticsearch:
        return [], 0
    search = current_app.elasticsearch.search(
        index=index,
        query={'multi_match': {'query': query, 'fields': ['*']}},
        from_=(page - 1) * per_page,
        size=per_page)
    ids = [int(hit['_id']) for hit in search['hits']['hits']]
    # returns the list of ids and the total number of results
    return ids, search['hits']['total']['value']