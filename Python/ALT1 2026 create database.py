import sqlite3

# BR1 Create a basic relational database
db = sqlite3.connect("school_clubs.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clubs (
    club_id INTEGER PRIMARY KEY,
    club_name TEXT,
    club_type TEXT,
    day TEXT,
    time TEXT,
    location TEXT,
    leader TEXT,
    spaces INTEGER
)
""")

# BR1 Add sample records
cursor.execute("""
INSERT INTO clubs
(club_name, club_type, day, time, location, leader, spaces)
VALUES (?, ?, ?, ?, ?, ?, ?)
""",
("Football", "Sport", "Monday", "4:00 PM",
 "Sports Hall", "Mr Smith", 10))

cursor.execute("""
INSERT INTO clubs
(club_name, club_type, day, time, location, leader, spaces)
VALUES (?, ?, ?, ?, ?, ?, ?)
""",
("Photography", "Creative", "Tuesday", "4:00 PM",
 "Room 12", "Ms Jones", 5))

cursor.execute("""
INSERT INTO clubs
(club_name, club_type, day, time, location, leader, spaces)
VALUES (?, ?, ?, ?, ?, ?, ?)
""",
("Chess", "Games", "Wednesday", "3:30 PM",
 "Library", "Mr Brown", 8))

db.commit()
db.close()