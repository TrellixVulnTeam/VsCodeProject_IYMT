# ��ARM64�㌚Tensorflow Lite

## ����

### �����H��

```bash
sudo apt-get update
sudo apt-get install crossbuild-essential-arm64
```

> �@�ʎg�pdocker�C�\�s���v����`sudo`

### ��

��Tensorflow��B�ݑ㍪�ډ��s���ʓI�r�{�����ˁF

> ��Ȏg�pdocker��`tensorflow/tensorflow:nightly-devel`�C
> tensorflow���`/tensorflow`

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

���ӑ����v��ꎟ������

:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

��o�꘢�Í݁F
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.

## ����

�ȉ��� HardKernel Odroid C2 �agcc 5.4.0�Ŗ{��.

�o�I�C�����H��

```bash
sudo apt-get install build-essential
```

���C��Tensorflow��B�ݑ㍪�ډ��s�F

```bash
./tensorflow/lite/tools/make/download_dependencies.sh
```

���ӑ����v��ꎟ������

:

```bash
./tensorflow/lite/tools/make/build_aarch64_lib.sh
```

��o�꘢�Í݁F
`tensorflow/lite/tools/make/gen/aarch64_armv8-a/lib/libtensorflow-lite.a`.
