import sqlite3 as sql

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.close()

def createTable():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budget_tracking (
            budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
            planning_id INTEGER,
            amount_spent DECIMAL(10,2) DEFAULT 0,
            amount_remaining DECIMAL(10,2),
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (planning_id) REFERENCES experience_planning(planning_id)
        );        
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    createTable()
