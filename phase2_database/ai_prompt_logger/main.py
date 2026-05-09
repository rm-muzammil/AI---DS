from fastapi import FastAPI
import psycopg2

app = FastAPI()

conn = psycopg2.connect(
    "postgresql://neondb_owner:npg_1LQDsYdIh5UG@ep-dawn-cloud-a1asvey3-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

@app.post("/prompt")
def save_prompt(prompt: str):
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO prompts (prompt) VALUES (%s)",
        (prompt,)
    )

    conn.commit()

    return {"message": "Prompt saved successfully"}

@app.get("/prompts")
def get_prompts():
    cur = conn.cursor()

    cur.execute("SELECT id, prompt, created_at FROM prompts")
    
    rows = cur.fetchall()
    
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "prompt": row[1],
            "created_at": row[2]
        })  
        
    return {"prompts": results}

@app.get("/stats")
def get_stats():

    cur = conn.cursor()

    # total prompts
    cur.execute("SELECT COUNT(*) FROM prompts")
    total = cur.fetchone()[0]

    # latest prompt
    cur.execute("""
        SELECT prompt
        FROM prompts
        ORDER BY created_at DESC
        LIMIT 1
    """)
    latest = cur.fetchone()

    # average prompt length
    cur.execute("""
        SELECT AVG(LENGTH(prompt))
        FROM prompts
    """)
    avg_length = cur.fetchone()[0]

    return {
        "total_prompts": total,
        "latest_prompt": latest,
        "avg_prompt_length": avg_length
    }
    
@app.get("/top-keywords")
def top_keywords():

    cur = conn.cursor()

    cur.execute("SELECT prompt FROM prompts")

    rows = cur.fetchall()

    text = " ".join([row[0] for row in rows])

    words = text.lower().split()

    from collections import Counter

    common = Counter(words).most_common(10)

    return {"top_keywords": common}

@app.get("/activity")
def activity():

    cur = conn.cursor()

    cur.execute("""
        SELECT DATE(created_at), COUNT(*)
        FROM prompts
        GROUP BY DATE(created_at)
        ORDER BY DATE(created_at)
    """)

    rows = cur.fetchall()

    result = []

    for r in rows:
        result.append({
            "date": str(r[0]),
            "count": r[1]
        })

    return result