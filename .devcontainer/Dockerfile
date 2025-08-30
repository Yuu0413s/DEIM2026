FROM debian:bullseye-slim

# 環境変数
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=ja_JP.UTF-8
ENV TZ=Asia/Tokyo

# 必要パッケージのインストールとシステム設定
RUN apt-get update && apt-get install -y --no-install-recommends \
   # 基本ツール
   git \
   curl \
   make \
   wget \
   ca-certificates \
   xdg-utils \
   # 日本語
   locales \
   fonts-ipaexfont \
   # TeXLive基本パッケージ
   texlive-base \
   texlive-lang-japanese \
   texlive-latex-recommended \
   texlive-latex-extra \
   texlive-extra-utils \
   latexmk \
   texlive-xetex \
   # Perlモジュールビルド用ツール（後で削除）
   build-essential \
   # ロケールとタイムゾーン設定
   && sed -i -e 's/# ja_JP.UTF-8 UTF-8/ja_JP.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen \
   && ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
   # Perlモジュールインストール
   && curl -L https://cpanmin.us | perl - App::cpanminus \
   && cpanm --no-wget \
   Log::Log4perl \
   Log::Dispatch::File \
   YAML::Tiny \
   File::HomeDir \
   Unicode::GCString \
   # 不要になったビルドツールの削除
   && apt-get purge -y build-essential \
   && apt-get autoremove -y \
   # キャッシュ削除でサイズ最適化
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/*

# TeX Liveのユーザーツリー初期化と日本語フォント設定
RUN tlmgr init-usertree \
   && kanji-config-updmap-sys ipaex

# デフォルトのlatexmkrc配置
COPY .latexmkrc /root/.latexmkrc

# 作業ディレクトリ設定
WORKDIR /workdir

# ヘルスチェック設定
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
   CMD pdflatex --version || exit 1

# デフォルトシェル
CMD ["bash"]