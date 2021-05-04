from csv import reader
import jsonlines
import os
import random
import shutil


def reformat_labels(input_file_name, output_file_name):
    """ Reformates election memes datatset to work with mmf framework """

    with open(input_file_name, mode='r') as file:
        csv_reader = reader(file)
        header = next(csv_reader)
        if header != None:
            with jsonlines.open(output_file_name, mode='w') as writer:
                for row in csv_reader:
                    data = {}
                    old_image_name,text, label = row

                    # Determine if file is png or jpg
                    # Previously they were almost all saved with .png file extension, but some were actually not in that format
                    # Converted into correct format with bash command
                    # file *.png | grep -i jpg | sed 's/:.*//' | while read -r f; do mv -- "$f" "${f%.png}.jpg"; done
                    image_directory = os.path.dirname(os.path.dirname(input_file_name)) + "/Labelled Images"
                    if not os.path.exists(image_directory + "/" + old_image_name):
                        image_name = old_image_name.split(".png")[0] + ".jpg"
                    else:
                        image_name = old_image_name
                    # print(old_image_name)
                    # print(image_name)

                    # Image name has to be an integer for mmf (cannot be string)
                    # Copy image file
                    source = image_directory + "/" + image_name
                    destination_dir = os.path.dirname(image_directory) + "/copied_images/"
                    if not os.path.exists(destination_dir):
                        os.makedirs(destination_dir)
                    destination = destination_dir + image_name

                    # print(source)
                    # print(destination)

                    shutil.copy(source, destination)

                    # Rename image file
                    split_name_list = image_name.split(".")
                    new_image_name = str(random.randint(1000000, 9999999)) + "." + split_name_list[1]
                    os.rename(destination_dir + image_name, destination_dir + new_image_name)

                    # Convert to mmf format
                    data["id"] = new_image_name.split(".png")[0].split(".jpg")[0]
                    data["img"] = "election_memes/" + new_image_name
                    data["label"] = 1 if label == "offensive" else 0
                    data["text"] = text

                    writer.write(data)

            writer.close()

if __name__ == "__main__":
    reformat_labels("/home/cathy/Downloads/election_memes/Split Dataset/Training_meme_dataset.csv", "train_election.jsonl")
    reformat_labels("/home/cathy/Downloads/election_memes/Split Dataset/Validation_meme_dataset.csv", "dev_election.jsonl")
    reformat_labels("/home/cathy/Downloads/election_memes/Split Dataset/Testing_meme_dataset.csv", "test_election.jsonl")
