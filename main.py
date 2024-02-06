from PIL import Image
import os
import glob

def is_file_present(directory, file_name):
    if os.path.exists(directory) and os.path.isdir(directory):
        # Check if the specified file is present in the directory
        if file_name in os.listdir(directory):
            return True
        else:
            return False
    else:
        return False

def list_folders(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]
        return folders
    else:
        return []
def make_pdf_all(dir_path):
    join = str("\\")
    dir_files = [dir_path + join + f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    return dir_files

def make_pdf_only_selected(selected_files, file_name, pdf_location):
    images_list = []
    for f in selected_files:
        try:
            images_list.append((Image.open(f)).convert('RGB'))
        except IOError:
            pass
    os.chdir(pdf_location)
    file_path = os.path.join(pdf_location, file_name + ".pdf")
    images_list[0].save(file_path, save_all=True, append_images=images_list[1:])

if __name__ == '__main__':
    #root directory
    dir_path="C:\\Users\\macro\\Documents\\Mangas\\"
    #destination directory
    pdf_location = "C:\\Users\\macro\\Desktop\\PDF"
    folders_found = list_folders(dir_path)
    for folder in folders_found:
        dirs = list_folders(dir_path+"\\"+folder)
        if is_file_present(pdf_location, folder) == False:
            os.makedirs(pdf_location+"\\"+folder)
            print("cartella creata")
        for dir in dirs:
            file_name = folder + " " + dir
            if is_file_present(pdf_location+"\\"+folder, file_name+".pdf")==False:
                make_pdf_only_selected(make_pdf_all(dir_path+"\\"+folder+"\\"+dir), file_name, pdf_location+"\\"+folder)
                print(file_name + " creato")





