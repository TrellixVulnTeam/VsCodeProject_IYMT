# �� iOS �㌚ TensorFlow Lite

�{�����`�q���@���� TensorFlow Lite iOS �B�@�ʎ��g�p�C�Ȓ��ڎg�p TensorFlow Lite CocoaPod �Ŗ{�B�Q [TensorFlow Lite iOS Demo](ios.md) �掦��B

## ��

TensorFlow Lite �I�ʗp iOS ���v�� MacOS �����C�� Xcode �I���ߍs�H����B
�@�ʖv�L�z�u�D���C�Ȓ� `xcode-select` ������ Xcode 8(���X���Ŗ{) �a�H��:

```bash
xcode-select --install
```

�@�ʐ���ꎟ�����C���v��s�ꎟ XCode �󓯈ӛ��I�B

(����v�����D [Homebrew](http://brew.sh/))

���ʈ��� [automake](https://en.wikipedia.org/wiki/Automake)/[libtool](https://en.wikipedia.org/wiki/GNU_Libtool):

```bash
brew install automake
brew install libtool
```

�@�ʋ����� automake  �a libtool �߈����A�����ړI�C�����ȉ�����:
```bash
sudo chown -R $(whoami) /usr/local/*
```
�R�@�g�p���ʓI���ߗ��g�ڐ���:
```bash
brew link automake
brew link libtool
```

�ڒ����p�� shell �r�{���������I��:
```bash
tensorflow/lite/tools/make/download_dependencies.sh
```

�㤏��a�����I���C�������`tensorflow/lite/downloads`��

���L�I�˓s�ߌ����C�݉ȍ� iOS ��ܘ��x���I�̌n�ˌ�:

```bash
tensorflow/lite/tools/make/build_ios_universal_lib.sh
```

���g�p `tensorflow/lite` ���I makefile �����s���Ŗ{�I�C�R�@�p `lipo` ��������� armv7, armv7s, arm64, i386, �a x86_64 �˓I�ʗp�������B�����I��: `tensorflow/lite/tools/make/gen/lib/libtensorflow-lite.a`

�@�ʍݍs `build_ios_universal_lib.sh` �C�������@ `no such file or directory: 'x86_64'` �I:
�� Xcode > Preferences > Locations�C�ۍ�"Command Line Tools"���f�ؒ��L�꘢���B

## �ݗp���g�p

���v�X�V�ꍱ�I�p�u���� TensorFlow Lite�B�ȍݎ����
`tensorflow/lite/examples/ios/simple/simple.xcodeproj` �ō��u�C
�A���ʒ񋟗��꘢�����I�v:

-   ���v�� `tensorflow/lite/gen/lib/libtensorflow-lite.a` �����I�ڌ��i�C�󊎍� Search Paths �I Library Search Paths �u���Y�� `tensorflow/lite/gen/lib`

-   _Header Search_ �H�a���v���:

    -   tensorflow �I����,
    -   `tensorflow/lite/downloads`
    -   `tensorflow/lite/downloads/flatbuffers/include`

-   �u `C++ Language Dialect`  `GNU++11` (�� `GNU++14`), ���u `C++ Standard Library`  `libc++` ���p C++11 �x�� (���X���Ŗ{)
