# slim_tex_env

## 動作確認環境

- MacbookAir2022 (OS version : macOS 15.6.1)
- Visual-Studi-Code (version : 1.103.2) ※以降 VSCode
- Docker(version : 28.3.3)
- Dev Containers(version : 0.422.1)

## 概要

ローカルでLaTeXを用いて文書を編集するためのDockerやVSCodeの設定ファイル群です。

この設定ファイルを任意の場所に配置し、VSCode上で操作を行えば、VScodeを編集ツールとして、LaTeXが動作するようにしてあります。

着想は korosuke613/texlive-ja-devcontainer-templateより得ています。
そちらがVSCodeのバージョンアップデートにより動作しなくなってしまったため、同等の機能を持ったものを再現するために作成したものとなっています。

ご許可をくださったkorosuke613様、誠にありがとうございます。

## 手順

VSCodeとDockerはbrewなどを経由してインストールしてある前提です。

1. VSCodeの拡張機能のDev-Containerをインストールする
2. LaTeX環境を作りたいディレクトリで、git cloneコマンドなどを用いてこのリポジトリのファイルをコピーする。
3. VSCode上のポップアップ(右下)が出てくるはずなので、「コンテナで再度開く」を選択する。
4. 十分な回線速度があれば3,4分ほどでコンテナが完成する。
5. 自動的にコンテナ内部に接続された状態になるので、sample.texなどをコンパイルしてみよう！
