import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()

    # This query calculates statistics per driver nationality.
    # First CTE (avg_points_for_each_nation) computes the average points per nationality from drivers_updated.
    # Second CTE (fastest_lap_for_each_nation) finds the minimum fastest lap time per nationality by joining drivers_updated with fastest_laps_updated.
    # Third CTE (most_recent_win_for_each_nation) finds the most recent win date per nationality by joining drivers_updated with winners.
    # The main query then LEFT JOINs all three CTEs on nationality to return, for each nationality:
    # - avg_pts: average points
    # - min_time: fastest lap
    # - latest: most recent win
    # LEFT JOIN ensures that nationalities without fastest laps or wins still appear, with NULL in those columns.

    cursor.execute("""
        WITH avg_points_for_each_nation AS (
            SELECT Nationality, AVG(PTS) as avg_pts
            FROM drivers_updated
            GROUP BY Nationality
        ),
        fastest_lap_for_each_nation AS (
            SELECT Nationality, MIN(f.Time) fastest_lap
            FROM drivers_updated d JOIN fastest_laps_updated f ON d.Driver = f.Driver
            GROUP BY d.Nationality
        ),
        most_recent_win_for_each_nation AS (
            SELECT d.Nationality, MAX(w.Date) AS recent_date
            FROM drivers_updated d
            JOIN winners w ON d.Driver = w.Winner
            GROUP BY d.Nationality
        )
        SELECT a.Nationality Nationality, a.avg_pts avg_pts, f.fastest_lap min_time, m.recent_date latest
        FROM avg_points_for_each_nation a LEFT JOIN fastest_lap_for_each_nation f ON a.Nationality = f.Nationality 
        LEFT JOIN most_recent_win_for_each_nation m ON a.Nationality = m.Nationality
""")
    print(', '.join(str(row) for row in cursor.fetchall()))
    cursor.close()
    mydb.close()