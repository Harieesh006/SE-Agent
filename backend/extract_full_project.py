import json
import os

with open("debug/broken_json.txt", "r", encoding="utf-8") as f:
    raw_content = f.read()

start_idx = raw_content.find('"files"')
files_start = raw_content.find('[', start_idx)
files_end = raw_content.rfind('}')

if files_start != -1 and files_end != -1:
    files_portion = raw_content[files_start:files_end+1]
    
    try:
        data = json.loads(files_portion)
        print(f"✅ Parsed {len(data)} files")
        
        project_root = "generated_project"
        os.makedirs(project_root, exist_ok=True)
        
        files_created = 0
        for file_info in data:
            filepath = os.path.join(project_root, file_info["path"])
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(file_info["content"])
                files_created += 1
                print(f"✅ {filepath}")
            except Exception as e:
                print(f"⚠️  {filepath}")
        
        print(f"\n✅ Created {files_created} files")
        
    except json.JSONDecodeError as e:
        print(f"Parse error at line {e.lineno}: {e.msg}")
