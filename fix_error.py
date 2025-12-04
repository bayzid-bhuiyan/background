import os

# 1. Rename app.py to main.py if it exists
if os.path.exists("app.py"):
    os.rename("app.py", "main.py")
    print("✅ Renamed app.py to main.py")
else:
    print("ℹ️ app.py not found (maybe already renamed)")

# 2. Force Procfile to point to main:app
procfile_content = "web: uvicorn main:app --host 0.0.0.0 --port $PORT"
with open("Procfile", "w", encoding="utf-8") as f:
    f.write(procfile_content)
print("✅ Fixed Procfile to use main:app")

print("\n🚀 Ready! Run the git commands below to push.")