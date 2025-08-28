from models.incep_xcep import IncepXcepFAS

def load_model(model_config):
    model_type = model_config.get('model_type', '')

    if model_type == 'IncepXcepFAS':
        return IncepXcepFAS()
    
    raise ValueError(f"Unknown model type: {model_type}")
