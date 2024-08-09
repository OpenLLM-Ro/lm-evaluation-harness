# Evaluation of RoLLMs

Official code used for evaluating Romanian LLMs. This repo is a fork of the popular [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) repo used for evaluation LLMs. On top of the existing framework we add a suite of Romanian benchmarks:

- ro_arc_challenge
- ro_mmlu
- ro_winogrande
- ro_hellaswag
- ro_gsm8k
- ro_truthfulqa
- ro_laroseda
- ro_wmt
- ro_xquad
- ro_sts
- ro_wiki



## Install

To install the `lm-eval` package from the github repository, run:

```bash
git clone https://github.com/EleutherAI/lm-evaluation-harness
cd lm-evaluation-harness
pip install -e .
```

We also provide a number of optional dependencies for extended functionality. A detailed table is available at the end of this document.

## Basic Usage
### User Guide

A user guide detailing the full list of supported arguments is provided [here](./docs/interface.md), and on the terminal by calling `lm_eval -h`. Alternatively, you can use `lm-eval` instead of `lm_eval`.

A list of supported tasks (or groupings of tasks) can be viewed with `lm-eval --tasks list`. Task descriptions and links to corresponding subfolders are provided [here](./lm_eval/tasks/README.md).

### Hugging Face `transformers`

To evaluate a model hosted on the [HuggingFace Hub](https://huggingface.co/models) (e.g. GPT-J-6B) on `hellaswag` you can use the following command (this assumes you are using a CUDA-compatible GPU):

```bash
lm_eval --model hf \
    --model_args pretrained=EleutherAI/gpt-j-6B \
    --tasks hellaswag \
    --device cuda:0 \
    --batch_size 8
```

Additional arguments can be provided to the model constructor using the `--model_args` flag. Most notably, this supports the common practice of using the `revisions` feature on the Hub to store partially trained checkpoints, or to specify the datatype for running a model:

```bash
lm_eval --model hf \
    --model_args pretrained=EleutherAI/pythia-160m,revision=step100000,dtype="float" \
    --tasks lambada_openai,hellaswag \
    --device cuda:0 \
    --batch_size 8
```

Models that are loaded via both `transformers.AutoModelForCausalLM` (autoregressive, decoder-only GPT style models) and `transformers.AutoModelForSeq2SeqLM` (such as encoder-decoder models like T5) in Huggingface are supported.

Batch size selection can be automated by setting the  ```--batch_size``` flag to ```auto```. This will perform automatic detection of the largest batch size that will fit on your device. On tasks where there is a large difference between the longest and shortest example, it can be helpful to periodically recompute the largest batch size, to gain a further speedup. To do this, append ```:N``` to above flag to automatically recompute the largest batch size ```N``` times. For example, to recompute the batch size 4 times, the command would be:

```bash
lm_eval --model hf \
    --model_args pretrained=EleutherAI/pythia-160m,revision=step100000,dtype="float" \
    --tasks lambada_openai,hellaswag \
    --device cuda:0 \
    --batch_size auto:4
```

> [!Note]
> Just like you can provide a local path to `transformers.AutoModel`, you can also provide a local path to `lm_eval` via `--model_args pretrained=/path/to/model`

## Advanced Usage Tips

For models loaded with the HuggingFace  `transformers` library, any arguments provided via `--model_args` get passed to the relevant constructor directly. This means that anything you can do with `AutoModel` can be done with our library. For example, you can pass a local path via `pretrained=` or use models finetuned with [PEFT](https://github.com/huggingface/peft) by taking the call you would run to evaluate the base model and add `,peft=PATH` to the `model_args` argument:
```bash
lm_eval --model hf \
    --model_args pretrained=EleutherAI/gpt-j-6b,parallelize=True,load_in_4bit=True,peft=nomic-ai/gpt4all-j-lora \
    --tasks openbookqa,arc_easy,winogrande,hellaswag,arc_challenge,piqa,boolq \
    --device cuda:0
```

We support wildcards in task names, for example you can run all of the machine-translated lambada tasks via `--task lambada_openai_mt_*`.



## Cite as


```bibtex
@misc{masala2024vorbecstiromanecsterecipetrain,
      title={"Vorbe\c{s}ti Rom\^ane\c{s}te?" A Recipe to Train Powerful Romanian LLMs with English Instructions}, 
      author={Mihai Masala and Denis C. Ilie-Ablachim and Alexandru Dima and Dragos Corlatescu and Miruna Zavelca and Ovio Olaru and Simina Terian and Andrei Terian and Marius Leordeanu and Horia Velicu and Marius Popescu and Mihai Dascalu and Traian Rebedea},
      year={2024},
      eprint={2406.18266},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.18266}, 
}
```

```bibtex
@misc{eval-harness,
  author       = {Gao, Leo and Tow, Jonathan and Abbasi, Baber and Biderman, Stella and Black, Sid and DiPofi, Anthony and Foster, Charles and Golding, Laurence and Hsu, Jeffrey and Le Noac'h, Alain and Li, Haonan and McDonell, Kyle and Muennighoff, Niklas and Ociepa, Chris and Phang, Jason and Reynolds, Laria and Schoelkopf, Hailey and Skowron, Aviya and Sutawika, Lintang and Tang, Eric and Thite, Anish and Wang, Ben and Wang, Kevin and Zou, Andy},
  title        = {A framework for few-shot language model evaluation},
  month        = 12,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.4.0},
  doi          = {10.5281/zenodo.10256836},
  url          = {https://zenodo.org/records/10256836}
}
```
