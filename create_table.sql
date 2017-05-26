DROP TABLE IF EXISTS handle CASCADE;
CREATE TABLE handle (
	handle_id integer NOT NULL,
	handle_name varchar NOT NULL
);


DROP TABLE IF EXISTS tweet CASCADE;
CREATE TABLE tweet (
	handle_id integer
		references handle(handle_id),
	timeTweeted date NOT NULL,
	PRIMARY KEY(timeTweeted, handle_id),
	favouriteCount integer NOT NULL,
	retweetCount integer,
	text varchar NOT NULL,
	originalAuthor varchar
);

DROP TABLE IF EXISTS hashtag CASCADE;
CREATE TABLE hashtag (
	tag varchar PRIMARY KEY
);

DROP TABLE IF EXISTS has CASCADE;
CREATE TABLE has (
	timeTweeted date NOT NULL,
	handle_id integer NOT NULL,
	FOREIGN KEY (timeTweeted, handle) 
		references tweet(timeTweeted, handle),
	tag varchar
		references hashtag(tag)
);
