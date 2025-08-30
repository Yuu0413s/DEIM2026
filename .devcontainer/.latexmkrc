#!/usr/bin/env perl

# 基本設定
$pdf_mode = 3;                    # PDF作成モードで (dvipdfmx)
$max_repeat = 3;                  # 最大反復回数を定義
$do_cd = 1;                       # 現在の作業ディレクトリをソースファイルのディレクトリに
$sleep_time = 1;                  # ビルド間の待機時間を定義

# エンジン設定
$latex = 'uplatex %O -halt-on-error -synctex=1 -interaction=nonstopmode -kanji=utf8 -file-line-error %S';
$pdflatex = 'pdflatex %O -halt-on-error -synctex=1 -interaction=nonstopmode -file-line-error %S';
$lualatex = 'lualatex %O -halt-on-error -synctex=1 -interaction=nonstopmode -file-line-error %S';
$xelatex = 'xelatex %O -halt-on-error -synctex=1 -shell-escape -interaction=nonstopmode -file-line-error %S';

# 文献処理
$biber = 'biber %O --bblencoding=utf8 -u -U --output_safechars %B';
$bibtex = 'upbibtex %O %B';

# インデックス処理
$makeindex = 'upmendex %O -o %D %S';

# 変換設定
$dvipdf = 'dvipdfmx %O -q -o %D %S';  # -q で静寂モード
$dvips = 'dvips %O -q -z -f %S | convbkmk -u > %D';
$ps2pdf = 'ps2pdf %O %S %D';

# PDFビューワ設定
$pdf_previewer = 'xdg-open %S';

# 差分検出の最適化
$pdf_update_method = 4;
$force_mode = 0;                  # 不要な再コンパイル抑制

# クリーンアップ設定
$clean_ext = 'aux bbl log out toc brf lof lot lol run.xml bcf synctex.gz dvi xdv nav snm vrb figlist makefile fdb_latexmk upa upb';

# プレビュー継続モード用の最適化
$pvc_view_file_via_temporary = 0;
$pvc_timeout = 30;

# 条件付き最適化（draft モード）
if ($ARGV[0] && $ARGV[0] =~ /draft/i) {
    $pdf_mode = 1;                # pdflatexモード
    print "Draft mode: Using pdflatex for faster compilation\n";
}