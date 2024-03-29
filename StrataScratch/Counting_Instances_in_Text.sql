/*
https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=1

Find the number of times the words 'bull' and 'bear' occur in the contents. We're counting the number of times
the words occur so words like 'bullish' should not be included in our count.
Output the word 'bull' and 'bear' along with the corresponding number of occurrences.

Table: google_file_store
*/

SELECT word,
    nentry
FROM ts_stat(
        'SELECT to_tsvector(contents) FROM google_file_store'
    )
WHERE word ILIKE 'bull'
    or word ILIKE 'bear'