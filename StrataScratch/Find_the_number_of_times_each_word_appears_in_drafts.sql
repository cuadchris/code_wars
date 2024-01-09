/*
Find the number of times each word appears in drafts.
Output the word along with the corresponding number of occurrences.

Table: google_file_store
*/

SELECT word,
    nentry
FROM ts_stat(
        'SELECT to_tsvector(contents) FROM google_file_store where filename ILIKE ''draft%'''
    )