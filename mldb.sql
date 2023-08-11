create database mldb;
use mldb;
CREATE TABLE music_library (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    album VARCHAR(255),
    genre VARCHAR(100),
    release_year INT
);
CREATE TABLE artists (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL,
    nationality VARCHAR(100),
    date_of_birth DATE
);
CREATE TABLE albums (
    album_id INT AUTO_INCREMENT PRIMARY KEY,
    album_title VARCHAR(255) NOT NULL,
    release_date DATE,
    record_label VARCHAR(100),
    album_cover VARCHAR(255)
);
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(100) NOT NULL
);

CREATE TABLE playlist (
    playlist_id INT PRIMARY KEY,
    playlist_name VARCHAR(255) NOT NULL,
    created_date DATE,
    -- Foreign keys to reference other tables
    song_id INT,
    artist_id INT,
    album_id INT,
    genre_id INT,
    FOREIGN KEY (song_id) REFERENCES music_library(id),
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id),
    FOREIGN KEY (album_id) REFERENCES albums(album_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);


SHOW TABLES;
select * from music_library;
select * from artists;
select * from playlists;
INSERT INTO music_library (title, artist, album, genre, release_year)
VALUES
    ('Song 1', 'Artist 1', 'Album 1', 'Genre 1', 2020),
    ('Song 2', 'Artist 2', 'Album 2', 'Genre 2', 2019),
    ('Song 3', 'Artist 3', 'Album 3', 'Genre 1', 2021),
    ('Song 4', 'Artist 1', 'Album 2', 'Genre 3', 2018),
    ('Song 5', 'Artist 4', 'Album 4', 'Genre 2', 2022),
    ('Song 6', 'Artist 2', 'Album 1', 'Genre 4', 2017),
    ('Song 7', 'Artist 5', 'Album 3', 'Genre 3', 2021),
    ('Song 8', 'Artist 3', 'Album 4', 'Genre 1', 2019),
    ('Song 9', 'Artist 1', 'Album 3', 'Genre 2', 2023),
    ('Song 10', 'Artist 2', 'Album 4', 'Genre 4', 2022);
    INSERT INTO artists (artist_name, nationality, date_of_birth)
VALUES
   ('Artist 1', 'Country A','1990-01-15'),
    ('Artist 2', 'Country B','1985-03-20'),
    ('Artist 3', 'Country C','1995-08-10'),
    ('Artist 4', 'Country B','1988-05-05'),
    ('Artist 5', 'Country D','1992-12-25'),
    ('Artist 6', 'Country A','1987-09-18'),
    ('Artist 7', 'Country C','1993-04-30'),
    ('Artist 8', 'Country B','1989-11-08'),
    ('Artist 9', 'Country D','1991-06-12'),
    ('Artist 10', 'Country A','1994-02-22');
    INSERT INTO albums (album_title, release_date, record_label, album_cover)
VALUES
    ('Album Title 1', '2023-07-15', 'Record Label A', 'album1_cover.jpg'),
    ('Album Title 2', '2022-11-20', 'Record Label B', 'album2_cover.jpg'),
    ('Album Title 3', '2021-04-05', 'Record Label C', 'album3_cover.jpg'),
    ('Album Title 4', '2020-09-30', 'Record Label A', 'album4_cover.jpg'),
    ('Album Title 5', '2019-02-10', 'Record Label B', 'album5_cover.jpg'),
    ('Album Title 6', '2018-06-25', 'Record Label C', 'album6_cover.jpg'),
    ('Album Title 7', '2017-10-12', 'Record Label A', 'album7_cover.jpg'),
    ('Album Title 8', '2016-03-28', 'Record Label B', 'album8_cover.jpg'),
    ('Album Title 9', '2015-08-02', 'Record Label C', 'album9_cover.jpg'),
    ('Album Title 10', '2014-12-15', 'Record Label A', 'album10_cover.jpg');
INSERT INTO genres (genre_name)
VALUES
    ('Genre 1'),
    ('Genre 2'),
    ('Genre 3'),
    ('Genre 4'),
    ('Genre 5'),
    ('Genre 6'),
    ('Genre 7'),
    ('Genre 8'),
    ('Genre 9'),
    ('Genre 10');
    
INSERT INTO playlist (playlist_id, playlist_name, created_date, song_id, artist_id, album_id, genre_id)
VALUES 
    (2, 'Chill Vibes', '2023-08-03', 3, 3, 1, 1),
    (3, 'Rock Classics', '2023-08-03', 4, 1, 2, 3),
    (4, 'Party Hits', '2023-08-03', 2, 5, 4, 2),
    (5, 'Feel Good', '2023-08-03', 8, 2, 3, 1),
    (6, 'Country Roads', '2023-08-03', 6, 4, 2, 4),
    (7, '90s Throwback', '2023-08-03', 5, 3, 5, 2);



show  tables;
select * from albums;
select * from artists;
select * from genres;
select * from music_library;
select * from playlist;
select artist_name,  album_title from artists a, albums b, playlist p, genres g where p.album_id=b.album_id and p.artist_id=a.artist_id and p.genre_id=g.genre_id and g.genre_id=2;
select count(*) from playlist p,artists a,albums al where p.artist_id=a.artist_id and al.album_id=p.album_id and a.artist_id=5;