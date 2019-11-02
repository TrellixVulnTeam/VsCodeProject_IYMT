# ���� C++ 

���T����� TensorFlow Lite C++ ��
[TensorFlow ](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro)
�I�ꕔ���B���A�ՏC���C�ʗǍD�C�Ր����C�󊎗^�y TensorFlow Lite ���e�B

���ʓI������o�� C++ �I��{�C�񋟗������I���߁C��o���������ʓ��V�I�T�B

��
[README.md](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/README.md#�@�����p�����T����ITensorFlow-Lite�ʓ��꘢�V�I����)
����܍X�������L���I�X���[���M���B

## ����

��
[`micro`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro)
���ڒ��L�꘢���I�B�R���C�����ʘ�����I TensorFlow ���C���ȉ䌚���ꍱ�r�{�a�����I�ڕ����C���Ɠ������i�@ Arduino, Keil, Make �a Mbed�j�񋟕��I���������B

### ����

�g�p���T����� TensorFlow Lite ����ŏd�v�I�����ݖړI���ڒ��C�󕍁F

-   [`all_ops_resolver.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/kernels/all_ops_resolver.h)
    �񋟉���s�͌^�I�Z���B
-   [`micro_error_reporter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_error_reporter.h)
    �o�M���B
-   [`micro_interpreter.h`](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/experimental/micro/micro_interpreter.h)
    ��܍T���a�s�͌^�I��B

�� [�n�g�p���T����](get_started.md) �ȝQ���T�^�I�p�r�I�W���B

���n�񋟖^�������ݓ��蕽��I�B���݈ȕ��䖼�̖����I�ډ��C��@�F
[`sparkfun_edge`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/sparkfun_edge)�B

�L�������ځC��F

-   [`kernel`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/kernels),
    ��܎Z���I�a����B
-   [`tools`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/tools),
    ��܌��H��a���I�o�B
-   [`examples`](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro/examples),
    ��܎����B

### �����ڕ���

�ڒ��I `Makefile` �\������܏��L�K���������I�Ɨ��ځC���������Ȕ���Ɠ������B�ڑO��x���I���� Arduino, Keil, Make �a Mbed�B

���ӁF�䑴���ꍱ����ǌ��ځB�Q
[�x���I����](overview.md#supported-platforms)
�ȉ��B

�v�� Make �������ځC�g�p�@���w�߁F

```bash
make -f tensorflow/lite/experimental/micro/tools/make/Makefile generate_projects
```

���v�{���C�������v���ꍱ��^�H��ˁB���@�C�œ����I�H�a���C�����ꍱ�����F
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/` �i�ؓI�H�a��r���I�������n�j�B��������ܐ����I�ژa�������B��@�F
`tensorflow/lite/experimental/micro/tools/make/gen/linux_x86_64/prj/keil`
��ܗ� Keil uVision �ځB

## ��

�@�ʍݎg�p�꘢�ߐ����I�ځC�Q�����ܓI README �Ȏ挚�w��B

�v���󘸎� TensorFlow �����s�C�s�ȉ����߁F

1.  �� GitHub ���c TensorFlow �����������֓I�n���B

    ```bash
    git clone --depth 1 https://github.com/tensorflow/tensorflow.git
    ```

2.  ����ꌚ�I�ځB

    ```bash
    cd tensorflow
    ```

3.  �p `Makefile` �����ڛ�s�B
    ���ӏ�����L���v�I�ˁF

    ```bash
    make -f tensorflow/lite/experimental/micro/tools/make/Makefile test
    ```

## �ʓ��V

�c���T����� TensorFlow Lite �ʓ��V����a�I�w��C��
[README.md](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/experimental/micro#�@�����p�����T����ITensorFlow-Lite�ʓ��꘢�V�I����)
���ŁB
