CUDA_VISIBLE_DEVICES=0 mbpo run_local examples.development --config=examples.config.halfcheetah.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=1 mbpo run_local examples.development --config=examples.config.halfcheetah.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=2 mbpo run_local examples.development --config=examples.config.walker2d.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=3 mbpo run_local examples.development --config=examples.config.walker2d.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=4 mbpo run_local examples.development --config=examples.config.hopper.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=5 mbpo run_local examples.development --config=examples.config.hopper.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=6 mbpo run_local examples.development --config=examples.config.ant.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=7 mbpo run_local examples.development --config=examples.config.ant.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=0 mbpo run_local examples.development --config=examples.config.halfcheetah.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=1 mbpo run_local examples.development --config=examples.config.halfcheetah.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=2 mbpo run_local examples.development --config=examples.config.walker2d.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=3 mbpo run_local examples.development --config=examples.config.walker2d.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=4 mbpo run_local examples.development --config=examples.config.hopper.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=5 mbpo run_local examples.development --config=examples.config.hopper.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=6 mbpo run_local examples.development --config=examples.config.ant.0 --gpus=1 --trial-gpus=1 &\
CUDA_VISIBLE_DEVICES=7 mbpo run_local examples.development --config=examples.config.ant.0 --gpus=1 --trial-gpus=1