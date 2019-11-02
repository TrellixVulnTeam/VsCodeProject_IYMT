# �Q�^TensorFlow������

TensorFlow�}������ - �@�ʉ��������C��������TensorFlow�{�g�B tensorflow.org��I�������ȉ��{�F

* *API ����* [API ����](https://www.tensorflow.org/api_docs/)
  �R
  [TensorFlow ����](https://github.com/tensorflow/tensorflow)���I����������(docstring)����.
* *���q����* �������e[����](https://www.tensorflow.org/tutorials)�A
  [�w��](https://www.tensorflow.org/guide)�ȋy�����s����TensorFlow��I���e. ������ʘ�GitHub�I
  [tensorflow/docs](https://github.com/tensorflow/docs) (repository)��.
* *�Ћ�|* �����R�Ћ�|�I�w��a�����B���s�푶����
  [tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site) (repository)��.

�ꍱ [TensorFlow ��](https://github.com/tensorflow) �������������ۑ��ݓƓI�����C�ʏ�ʘ�`docs/`�ڒ��B �Q�ړI`CONTRIBUTING.md`�������n�҈ȎQ�^�B

�Q�^��TensorFlow�����Ћ�I�����L:

* ��GitHub���I [tensorflow/docs](https://github.com/tensorflow/docs) (repository).
*  [docs@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs).
* ���� [Gitter �֓V��](https://gitter.im/tensorflow/docs).

## API ����

�@�ʑz�X�VAPI�����C�Q�����I
[������](https://www.tensorflow.org/code/tensorflow/python/)
�󑊓I
<a href="https://www.python.org/dev/peps/pep-0257/" class="external">����������(docstring)</a>.
tensorflow.org��I��API ���p�I�ʓs��ܗ��w����������ʒu�I�ځB �����������x��
<a href="https://help.github.com/en/articles/about-writing-and-formatting-on-github" class="external">Markdown�i��</a>
�󊎁i�命����j�s�\�g�p
<a href="http://tmpvar.com/markdown.html" class="external">Markdown ��</a>
�s.

�L�Q�l�����ʈȋy�@���Q�^�����t�h�a�Ћ�C�Q
[TensorFlow 2.0 API������](https://docs.google.com/document/d/1e20k9CuaZ_-hp25-sSd8E8qldxKPKQR-SkwojYr_r-U/preview)�B

### �Ŗ{(Versions) �a ���x(Branches)

�{�⋓I [API ����](https://www.tensorflow.org/api_docs/python/tf)
�Ŗ{�ҍŐV�I��񐧕������^��`pip install tensorflow`�����I�Ŗ{���C�z.

�ғITensorFlow �����<a href="https://github.com/tensorflow/tensorflow" class="external">tensorflow/tensorflow</a>(repository)���I�蕪�x`rX.x`�����I�B�������R
<a href="https://www.tensorflow.org/code/tensorflow/python/" class="external">Python</a>�A
<a href="https://www.tensorflow.org/code/tensorflow/cc/" class="external">C++</a>�^
<a href="https://www.tensorflow.org/code/tensorflow/java/" class="external">Java</a>�㒆�I���^�����������������B

�ȑO�Ŗ{�ITensorFlow������TensorFlow Docs (repository)����[rX.x ���x](https://github.com/tensorflow/docs/branches) �I�`���񋟁B�ݕz�V�Ŗ{��Y�������x�B

### ��API����

���ӁF��API�����������s���v���C��������tensorflow.org��g�p�IHTML�B

#### Python ����

`tensorflow_docs`����[Python API ����](https://www.tensorflow.org/api_docs/python/tf)�I������B
���������F

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">pip install git+https://github.com/tensorflow/docs</code>
</pre>

�v����TensorFlow 2.0�����C�g�p
`tensorflow/tools/docs/generate2.py` �r�{:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone https://github.com/tensorflow/tensorflow tensorflow</code>
<code class="devsite-terminal">cd tensorflow/tensorflow/tools/docs</code>
<code class="devsite-terminal">pip install tensorflow</code>
<code class="devsite-terminal">python generate2.py --output_dir=/tmp/out</code>
</pre>

���ӁF���r�{�g�p*�߈���*�ITensorFlow��������󊎗p��TensorFlow 2.x.

## ���q����

TensorFlow [�w��](https://www.tensorflow.org/guide) �a
[����](https://www.tensorflow.org/tutorials) ����
<a href="https://guides.github.com/features/mastering-markdown/" class="external">Markdown</a>
�����a���ݎ��I
<a href="https://jupyter.org/" class="external">Jupyter</a> �{���ʁB �Ȏg�p
<a href="https://colab.research.google.com/notebooks/welcome.ipynb"
   class="external">Google Colaboratory</a>
�ݓI�풆�s�{�B
[tensorflow.org](https://www.tensorflow.org)���I���q����������
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>�I
`master` ���x��. ���Ŗ{���ݍ�GitHub (repository)���I`rX.x`�s�ŕ��x���B

### �X��

�s�����X�V�a�C�I�ŕ��@���g�pGitHub�I
<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">Web������</a>�B
[tensorflow/docs](https://github.com/tensorflow/docs/tree/master/site/en)
(repository) �ȝQ�^
<a href="https://www.tensorflow.org">tensorflow.org</a>
���IURL ���IMarkdown��notebook�����B �ݕ����I�E��p�C
<svg version="1.1" width="14" height="16" viewBox="0 0 14 16" class="octicon octicon-pencil" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
���ŕ�����B �����C�R�@���V�I�f�拁(pull request)�B

### �u�{�nGit(repository)

�����������X�I�X�V�C�ōD�g�p�{�nGit�H�여�����f�拁(pull request)�B

���ӁF<a href="https://git-scm.com/" class="external">Git</a> ���p�����H����X���I���Ŗ{�T���n�iVCS�j�B
<a href="https://github.com" class="external">GitHub</a>����ݕ��C
�񋟗^Git�z���g�p�I��H��B�Q<a href="https://help.github.com" class="external">GitHub Help</a>�Ȓu�IGitHub��n�g�p�B

���L�ݑ�ꎟ�u�{�n�ڍˎ��v�ȉ�Git�B

#### ��(fork) tensorflow/docs (repository)

��
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
�IGithub���C�_*Fork*��
<svg class="octicon octicon-repo-forked" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
�ݓIGitHub�������ȓI���{�B��(fork) �����C���v�ێ��I���{���{�^���TensorFlow�I���B

#### �����I(repository)

���� <var>username</var>/docs �I���{���{�n�Z���B���V�@�s����I�H��ځF

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git clone git@github.com:<var>username</var>/docs</code>
<code class="devsite-terminal">cd ./docs</code>
</pre>

#### �Y�����(upstream repo)�ȕێ��ŐV�i�j

�v�g�{�n���^`tensorflow/docs`�ێ����C���v�Y���꘢*���(upstream)*
�����ŐV�I�X���B

���ӁF�ۍݎn��e*�V�O*�X�V�I�{�n�B������������~��ݒ��f�拁(pull request)��<a href="https://help.github.com/articles/resolving-a-merge-conflict-using-the-command-line" class="external">����t��(merge conflict)</a>�I�\���B

�Y����:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git remote add <var>upstream</var> git@github.com:tensorflow/docs.git</code>

# ��
<code class="devsite-terminal">git remote -v</code>
origin    git@github.com:<var>username</var>/docs.git (fetch)
origin    git@github.com:<var>username</var>/docs.git (push)
<var>upstream</var>  git@github.com:tensorflow/docs.git (fetch)
<var>upstream</var>  git@github.com:tensorflow/docs.git (push)
</pre>

�X�V:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git checkout master</code>
<code class="devsite-terminal">git pull <var>upstream</var> master</code>

<code class="devsite-terminal">git push</code>  # Push changes to your GitHub account (defaults to origin)
</pre>

### GitHub �H�여

#### 1. ���꘢�V���x

��`tensorflow / docs`�X�V�I�@�C���{�n*master*���x�����꘢�V�I���x:

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git checkout -b <var>feature-name</var></code>

<code class="devsite-terminal">git branch</code>  # ��o�{�n���x
  master
* <var>feature-name</var>
</pre>

#### 2. ��X��

�݊�I�풆�����C�󏅎�
[TensorFlow�������w��](./docs_style.md)�B

��𕶌��X���F

<pre class="prettyprint lang-bsh">
# �ōX��
<code class="devsite-terminal">git status</code>  # �ō�������C��
<code class="devsite-terminal">git diff</code>    # �ŕ������I�X�����e

<code class="devsite-terminal">git add <var>path/to/file.md</var></code>
<code class="devsite-terminal">git commit -m "Your meaningful commit message for the change."</code>
</pre>

�������v�Y���X������B

#### 3. ���꘢�f�拁(pull request)

���I�{�n���x�㓞�I��GitHub
(github.com/<var>username</var>/docs):

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">git push</code>
</pre>

���������@�C�����\��꘢URL�C�Ȏ�����������f�拁�B�@�ʖv�L�C��
<a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
���Ҏ��ȓIGitHub���񎦌��f�拁(pull request)�B

#### 4. �Z

�Ҙa�������ҏ��j�I�f�拁(pull request)�B�Q�^�󍪐��v���s�C���B���I������y�@�C�������󓞏��TensorFlow�������B

�����@�F�I�X�����TensorFlow�����ڎ�B

��GitHub�X�V
[tensorflow.org](https://www.tensorflow.org)���꘢�ƓI�B�ʏ��v���C�����X�������󗝁C�����㎊�⋒��B

## ���ݎ��{�inotebook�j

�R�Ȏg�pGitHub�I<a href="https://help.github.com/en/articles/editing-files-in-your-repository" class="external">web���{��</a>���{JSON�����C�A�s��䦎g�p���C���i���IJSON�\������B �ۍݒ��f�拁(pull request)�V�O�{�B

<a href="https://colab.research.google.com/notebooks/welcome.ipynb" class="external">Google Colaboratory</a>
���꘢��ǖ{���C�ȏ��a�s�{�����B GitHub���I�{�ʏ��H�aColab URL�i��@�C�ʘ�GitHub���I�{�j��Google Colab�����F
<a href="https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https&#58;//github.com/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a><br/>
�Ȓʈȉ�URL�ڍ�Google Colab����:
<a href="https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb">https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/basic_classification.ipynb</a>

�L�꘢
<a href="https://chrome.google.com/webstore/detail/open-in-colab/iogfkhleblhcpcekbiedikdehleodpjo" class="external">Open in Colab</a>
�W�����C�ȍ�GitHub��{�s��URL�ցB �ݐ��I�����Ŗ{���L�p�C�����n�ړ�TensorFlow Docs�I`master`���x�B

### ��Colab

��Google Colab�����C�o���i�ȕ��{�a��B���{���i�g�pMarkdown�i���C���z
[TensorFlow�������w��](./docs_style.md).

�ʓ_ *File > Download .pynb* �Ș�Colab�����{�����B ����������𓞓I[�{�nGit](###�u�{�nGit(repository))�@�Ē��f�拁�B

�@���v���V�{�C���a
<a href="https://github.com/tensorflow/docs/blob/master/tools/templates/notebook.ipynb" external="class">TensorFlow �{�͔�</a>.

### Colab-GitHub�H�여

�Ȓ��ژ�Google Colab�a�X�V���IGitHub�C���s�����{������g�p�{�nGit�H�여�F

1. �ݐ�(fork)�I <var>username</var>/docs ���C�g�pGitHub Web�E��
   <a href="https://help.github.com/articles/creating-and-deleting-branches-within-your-repository" class="external">���V���x</a>�B
2. �q���v�I�{�����B
3. ��Google Colab���Ŗ{�F�g�pURL�ֈ�*Open in Colab* Chrome�W�����B
4. ��Colab���{�B
5. �ʓ_
   *File > Save a copy in GitHub...*��Colab����GitHub����X���B�ۑ��y�������I�^���x�B��Y�����L�ӓI��������B
6. �ۑ��V�@�C�I����
   <a href="https://github.com/tensorflow/docs" class="external">tensorflow/docs</a>
   �CGitHub��񎦌��꘢pull���B
7. �҉�j�I�f�拁(pull request)�B

�����@�F�I�X�����TensorFlow�����ڎ�B

## �Ћ�|

�Ћ�|��TensorFlow�ݑS���E�s�ȓI�D���@�B�@���X�V���Y���|�C��[����](https://github.com/tensorflow/docs/tree/master/site)����`en/`�����I�ڝQ�����Y���꘢�V�����B�p������*�Ŋ�*�I�����C�|�s�\�n���z���w��B��A���C�|�s�ʕێ����`�����B�@�ʉp�C�Z�C�i�����s�\�|���������C�їp���ғI�|�B

���ӁF*�ܖ|* tensorflow.org���IAPI���p.

�L���蘰���I�����C�g�|���҉ȍX���n�s�B �@�ʐ���ҁC�҈������z�Ћ挚TensorFlow.org���e�C�����F

* �̒���: [docs-zh-cn@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-zh-cn)
* ��: [docs-ja@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ja)
* : [docs-ko@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ko)
* �╶: [docs-ru@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-ru)
* �y����: [docs-tr@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/docs-tr)

### �Z�m

���L�����X�V�s���v�j�B ���X�L���n�^TensorFlow�|�Ћ�s��C�ȉ����ꍱ�ێ������芈�I���@�F

* ������ʗ�o�I���C�Ȑڝ��C���y��<code><a
  href="https://github.com/tensorflow/docs/tree/master/site">site/<var>lang</var></a></code>�ړI*�ߌ��I* �f�拁�B
* ���IGitHub�p���Y����`site/<lang>/REVIEWERS`�����ݝf�拁���\�펩���B�ݔ�@�CGitHub������f�拁�����L�X���a�I�ʒm�B

### �ݖ|����ێ��ŐV

����TensorFlow�I���ځC�ێ������ŐV���꒧�B�ݗ^�Ћ��V�@�C�|���e�I�Ҕ\�e�E�L�_�I���{�C�A�I���l�S���B���X�e�Օێ��㓯�C�|�I�{�g�p
[nb-code-sync](https://github.com/tensorflow/docs/blob/master/tools/nb_code_sync.py)�H��F

<pre class="prettyprint lang-bsh">
<code class="devsite-terminal">./tools/nb_code_sync.py [--lang=en] site/<var>lang</var>/notebook.ipynb</code>
</pre>

���r�{�挾�{�I�㌳�i�C�󍪐��p�Ŗ{�s�B �����@�C�������X�V���{�i�@�ʛ��s���j�B ���H����ݎ�git�H�여���L�p�C�Ȑ��n�������Y�����X����: `git add --patch site/lang/notebook.ipynb`

## Docs sprint

�Q�����ߓI
[TensorFlow 2.0 Global Docs Sprint](https://www.google.com/maps/d/viewer?mid=1FmxIWZBXi4cvSy6gJUW9WRPfvVRbievf)
���C���������B ����
[���q����](https://medium.com/tensorflow/https-medium-com-margaretmz-tf-docs-sprint-cheatsheet-7cb1dfd3e8b5?linkId=68384164)�B���������nTensorFlow������o���I�D���@�B
