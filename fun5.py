skill={
    "css":"80%",
    "python":"70",
    "html":"60%"
}
def show_skills(**skill):
    print("hey friend your skill is ")
    for skii in skill:
        print(f"{skii}")
show_skills(**skill)