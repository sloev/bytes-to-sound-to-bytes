

from gtts import gTTS 

language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

adjectives = [
    'adorable', 'adventurous', 'alluring', 'amazing',
    'ambitious', 'amusing', 'astonishing', 'attractive', 'awesome',
    'bashful', 'bawdy', 'beautiful', 'bewildered', 'bizarre', 'bouncy',
    'brainy', 'brave', 'brawny', 'burly', 'capricious', 'careful',
    'caring', 'cautious', 'charming', 'cheerful', 'chivalrous',
    'classy', 'clever', 'clumsy', 'colossal', 'cool', 'coordinated',
    'courageous', 'cuddly', 'curious', 'cute', 'daffy', 'dapper',
    'dashing', 'dazzling', 'delicate', 'delightful', 'determined',
    'eager', 'embarrassed', 'enchanted', 'energetic', 'enormous',
    'entertaining', 'enthralling', 'enthusiastic', 'evanescent',
    'excited', 'exotic', 'exuberant', 'exultant', 'fabulous', 'fancy',
    'festive', 'finicky', 'flashy', 'flippant', 'fluffy', 'fluttering',
    'funny', 'furry', 'fuzzy', 'gaudy', 'gentle', 'giddy', 'glamorous',
    'gleaming', 'goofy', 'gorgeous', 'graceful', 'grandiose', 'groovy',
    'handsome', 'happy', 'hilarious', 'honorable', 'hulking',
    'humorous', 'industrious', 'incredible', 'intelligent', 'jazzy',
    'jolly', 'joyous', 'kind', 'macho', 'magnificent', 'majestic',
    'marvelous', 'mighty', 'mysterious', 'naughty', 'nimble', 'nutty',
    'oafish', 'obnoxious', 'outrageous', 'pretty', 'psychedelic',
    'psychotic', 'puzzled', 'quirky', 'quizzical', 'rambunctious',
    'remarkable', 'sassy', 'shaggy', 'smelly', 'sneaky', 'spiffy',
    'swanky', 'sweet', 'swift', 'talented', 'thundering', 'unkempt',
    'upbeat', 'uppity', 'wacky', 'waggish', 'whimsical', 'wiggly',
    'zany'
]
nouns = [
    'aardvarks', 'alligators', 'alpacas', 'anteaters', 'antelopes',
    'armadillos', 'baboons', 'badgers', 'bears', 'beavers',
    'boars', 'buffalos', 'bulls', 'bunnies', 'camels', 'cats',
    'chameleons', 'cheetahs', 'centaurs', 'chickens', 'chimpanzees',
    'chinchillas', 'chipmunks', 'cougars', 'cows', 'coyotes', 'cranes',
    'crickets', 'crocodiles', 'deers', 'dinasaurs', 'dingos', 'dogs',
    'donkeys', 'dragons', 'elephants', 'elves', 'ferrets', 'flamingos',
    'foxes', 'frogs', 'gazelles', 'giraffes', 'gnomes', 'gnus', 'goats',
    'gophers', 'gorillas', 'hamsters', 'hedgehogs', 'hippopotamus',
    'hobbits', 'hogs', 'horses', 'hyenas', 'ibexes', 'iguanas',
    'impalas', 'jackals', 'jackalopes', 'jaguars', 'kangaroos',
    'kittens', 'koalas', 'lambs', 'lemmings', 'leopards', 'lions',
    'ligers', 'lizards', 'llamas', 'lynxes', 'meerkat', 'moles',
    'mongooses', 'monkeys', 'moose', 'mules', 'newts', 'okapis',
    'orangutans', 'ostriches', 'otters', 'oxes', 'pandas', 'panthers',
    'peacocks', 'pegasuses', 'phoenixes', 'pigeons', 'pigs',
    'platypuses', 'ponies', 'porcupines', 'porpoises', 'pumas',
    'pythons', 'rabbits', 'raccoons', 'rams', 'reindeers',
    'rhinoceroses', 'salamanders', 'seals', 'sheep', 'skunks',
    'sloths', 'slugs', 'snails', 'snakes', 'sphinxes', 'sprites',
    'squirrels', 'takins', 'tigers', 'toads', 'trolls', 'turtles',
    'unicorns', 'walruses', 'warthogs', 'weasels', 'wolves',
    'wolverines', 'wombats', 'woodchucks', 'yaks', 'zebras'
]

for text in adjectives + nouns:
    print(text, flush=True)
    myobj = gTTS(text=text, lang=language, slow=True) 
    
    # Saving the converted audio in a mp3 file named 
    # welcome  
    myobj.save(f"words/{text}.mp3") 