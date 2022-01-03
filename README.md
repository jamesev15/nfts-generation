# nfts-generation
Generation of NFTS for integration with Opensea

## Code to generate all possible NTFS combinations from layers.

For this test we worked with the following layers:
- Backgrounds
- Breed
- Eyes

All possible combinations of layers from these directories were generated.

## Configuration

- In the "config.py" file, the order of overlapping of the layers must be placed, generally starting with the background.

- "Batch" is the amount of parallel image generation that can be processed.

- "exclude_files" are all files that are not additional layer directories in the project.

## Execute
python3 generate.py

The generated images are located in the directory "images".

Soon we will add the metadata in json for the integration with opensea.
