# 수정된 파일 내용이 임시로 저장될 리스트
edited_lines = []

with open("./custom-highlight-copy.js") as f:
    lines = f.readlines()
    for line in lines:
        # 조건에 따라 원하는 대로 line을 수정
        if 'name: "유학, 한화에어로스페이스"' in line:
            edited_lines.append('\t\t\t\tname: "유학, 한화에어로스페이스", data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434],\n')
        else:
            edited_lines.append(line)

with open("./custom-highlight-copy.js", 'w') as f:
    f.writelines(edited_lines)