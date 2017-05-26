DROP TABLE IF EXISTS tweet CASCADE;
CREATE TABLE tweet (
	timeTweeted date NOT NULL,
	handle boolean NOT NULL,
	PRIMARY KEY(timeTweeted, handle),
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
	handle boolean NOT NULL,
	FOREIGN KEY (timeTweeted, handle) 
		references tweet(timeTweeted, handle),
	tag varchar
		references hashtag(tag)
);


