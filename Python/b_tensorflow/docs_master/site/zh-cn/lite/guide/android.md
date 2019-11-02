# Android �������

�v��Android��g�pTensorFlow Lite�C�䐄䦒T�����ʓI��q�B

<a class="button button-primary" href="https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android">Android
��������</a>

�L����I���C
[TensorFlow Lite Android ����](https://www.tensorflow.org/lite/models/image_classification/android).

����p�����g�p
[����](https://www.tensorflow.org/lite/models/image_classification/overview)
���n�I�@�u�����œ��I���e�s���B
�p�����ȍs�ݐ^���Җ͊��B

�g�p TensorFlow Lite Java API ���s�����B�����p�����n���s���C���ŉ\�I���ʁB����p���_��
[�ʉ�](https://www.tensorflow.org/lite/performance/post_training_quantization)
�͌^�C�����C��r��s��CPU�CGPU��C��������
[NNAPI](https://developer.android.com/ndk/guides/neuralnetworks)�s�B

����: ��[����](https://www.tensorflow.org/lite/examples)�񋟗������I�ݑ��p�ᒆ�����g�pTensorFlow Lite�I�p�����B 

## ��Android Studio����

�@�ʗv��Android Studio ����q�C���z
[README.md](https://github.com/tensorflow/examples/blob/master/lite/examples/image_classification/android/README.md)���I���B

## �����ȓIAndroid�p����

�@�ʑz�����ʓIAndroid��, �䐄䦎g�p
[Android �������q](https://github.com/tensorflow/examples/tree/master/lite/examples/image_classification/android)
��N�n�_�B

���ʓI������ܗ��ꍱ�L�@����Android��g�pTensorFlow Lite�I�L�p�M���B

### �g�pJCenter���ITensorFlow Lite AAR

�@�ʗv�ݓIAndroid�p�������g�pTensorFlow Lite�C�䐄䦎g�p
[��JCenter����ǓITensorFlow Lite AAR](https://bintray.com/google/tensorflow/tensorflow-lite)�B

�ȑ����ʍݓI`build.gradle`�˒��w�蛀:

```build
dependencies {
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly'
}
```

��AAR��ܗ�
[Android ABIs](https://developer.android.com/ndk/guides/abis)���I���L�I�񐧕����B�Ȓʑ���܎��v�x���IABIs�����p�����I�񐧕����召�B

�䐄䦑啔���I�� `x86`�C`x86_64`�C�a`arm32` �IABIs�B�Ȓʔ@���IGradle�z�u�C���z�u����� `armeabi-v7a`�a`arm64-v8a`�C�z�u�\��᳏Z�啔���I��Android�B

```build
android {
    defaultConfig {
        ndk {
            abiFilters 'armeabi-v7a', 'arm64-v8a'
        }
    }
}
```

�z�v�����X���L `abiFilters`�I�M��, ��Android Gradle�������I
[`NdkOptions`](https://google.github.io/android-gradle-dsl/current/com.android.build.gradle.internal.dsl.NdkOptions.html)�B

### �ݖ{�n��TensorFlow Lite

�ݖ^����v���C�\��]�g�p�꘢�{�n���ITensorFlow Lite. ��@�C�\���݌��꘢����I��ܗ�
[��TensorFlow���I����](https://www.tensorflow.org/lite/guide/ops_select)�I�񐧕����B

�ݏ�v���C�Q��
[���� AAR ����](https://www.tensorflow.org/lite/guide/ops_select#android_aar)
�������ȓIAAR�󏫑���܍ݓIAPP��.
