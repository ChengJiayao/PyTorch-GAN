from os import listdir
from os.path import isfile, join

def save_model(generator, discriminator, model_save_dir, epoch):
    """Save the current generator and discriminator models (with the given epoch)."""
    torch.save(generator.state_dict(), model_save_dir + 'G_' + str(epoch))
    torch.save(discriminator.state_dict(), model_save_dir + 'D_' + str(epoch))
    print('Saved model checkpoints into {}...'.format(model_save_dir))


def load_model(generator, discriminator, path):
    """Load the most recent saved model into the generator and the discriminator."""
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    idx = 0
    if len(onlyfiles) > 0:
        idx = max([int(f.split('_')[1]) for f in onlyfiles])
        generator.load_state_dict(torch.load(path+'G_'+str(idx), map_location=lambda storage, loc: storage))
        discriminator.load_state_dict(torch.load(path + 'D_' + str(idx), map_location=lambda storage, loc: storage))
        print('Loading the trained models from step {}...'.format(idx))
    return generator, discriminator, idx