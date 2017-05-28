DROP TABLE IF EXISTS handle CASCADE;
CREATE TABLE IF NOT EXISTS handle (
	handle_id integer PRIMARY KEY,
	handle_name varchar
);


DROP TABLE IF EXISTS tweet CASCADE;
CREATE TABLE IF NOT EXISTS tweet (
	handle_id integer
		references handle(handle_id),
	timeTweeted timestamp NOT NULL,
	PRIMARY KEY(timeTweeted, handle_id),
	favouriteCount integer,
	retweetCount integer,
	text varchar NOT NULL,
	originalAuthor varchar
);

DROP TABLE IF EXISTS hashtag CASCADE;
CREATE TABLE IF NOT EXISTS hashtag (
	tag varchar PRIMARY KEY
);

DROP TABLE IF EXISTS has CASCADE;
CREATE TABLE IF NOT EXISTS has (
	timeTweeted timestamp NOT NULL,
	handle_id integer NOT NULL,
	FOREIGN KEY (timeTweeted, handle_id) 
		references tweet(timeTweeted, handle_id),
	tag varchar
		references hashtag(tag)
);
