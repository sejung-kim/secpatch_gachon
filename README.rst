.. _readme:

==================================
Verilator RISC-V Simulation Setup
==================================

이 문서는 Verilator 기반 RISC-V 시뮬레이션 환경을 구축하고,
Chipyard를 이용해 Rocket Core를 시뮬레이션하는 과정을 정리한 것입니다.

.. contents::
   :local:
   :depth: 2

1. Verilator Installation
=========================

1.1 Dependencies & Installation
-------------------------------
.. code-block:: bash

   sudo apt-get update
   sudo apt-get install verilator \
       git make autoconf g++ flex bison \
       libfl2 libfl-dev

1.2 GitHub 저장소 클론
----------------------
.. code-block:: bash

   git clone git@github.com:sejung-kim/secpatch_gachon.git
   cd secpatch_gachon
   unset VERILATOR_ROOT  # bash 환경에서 필요

1.3 Verilator 빌드 & 테스트
---------------------------
.. code-block:: bash

   autoconf
   ./configure
   make
   make test
   sudo make install  # 권한 문제 발생 시 sudo 사용

2. Chipyard Environment Setup
=============================

Chipyard는 Conda를 활용하여 RISC-V 툴체인 및 각종 의존성을 관리합니다.

2.1 Conda 기본 설정
--------------------
.. code-block:: bash

   conda install -n base conda-libmamba-solver
   conda config --set solver libmamba
   conda install -n base conda-lock==1.4.0
   conda activate base

2.2 Chipyard & RISC-V 툴체인 설치
---------------------------------
.. code-block:: bash

   # Chipyard 최상위 경로에서:
   ./build-setup.sh riscv-tools

   # 설치 완료 후 env.sh 파일 생성
   source ./env.sh

3. Rocket Core Simulation with Verilator
========================================

3.1 RocketConfig 생성
---------------------
Chipyard의 Verilator 시뮬레이션 디렉토리로 이동 후:

.. code-block:: bash

   cd chipyard/sims/verilator
   make

이 명령어로 **simulator-chipyard.harness-RocketConfig** 실행 파일이 생성됩니다.

3.2 RISC-V 바이너리 실행
------------------------
.. code-block:: bash

   make run-binary BINARY=chipyard/tests/build/<프로그램명>.riscv

4. Custom RISC-V Binary Simulation
==================================

1) chipyard/tests 폴더에 사용자 코드 추가  
2) CMakefile 내 PROGRAMS 리스트에 추가  
3) 바이너리 빌드 (make) 시 `.riscv` 파일 생성  
4) 아래와 같이 시뮬레이션 실행:

.. code-block:: bash

   cd chipyard/sims/verilator
   make run-binary BINARY=chipyard/tests/build/<user_program>.riscv

5. Waveform Analysis (GTKWave)
==============================

디버그 빌드를 통해 VCD 파일 생성 후 GTKWave로 확인 가능합니다.

.. code-block:: bash

   make run-binary-debug BINARY=chipyard/tests/build/<program>.riscv
   gtkwave <generated_file>.vcd

6. Experimental Results
=======================

6.1 Fibonacci 연산
------------------
- 약 0.8μs에 ibuf 신호가 바이너리 인스트럭션을 읽기 시작  
- 500μs~540μs 구간에서 버퍼에서 빈번한 R/W 동작 → 피보나치 연산 진행

6.2 GCD 연산
------------
- 모든 인스트럭션이 버퍼에 저장된 후 마지막에 연산  
- 중간 신호 비활성 구간은 연산 준비 단계로 분석  
- BootROM이 클록/리셋을 포함한 초기 제어 신호를 전달하여 코어를 구동

Rocket Core는 AXI 프로토콜을 통해 데이터 통신하며, Verilator 시뮬레이션을 통해 부트 과정을 비롯한 하드웨어 동작을 검증할 수 있습니다.

----

Additional Note
---------------
본 시뮬레이션 환경은 `Verilator <https://github.com/verilator/verilator>`_ 오픈 소스 프로젝트를 기반으로 구축되었습니다.

**문의**  
- 사용 방법 및 설치와 관련하여 추가 문의 사항이 있으시면 GitHub 이슈 또는 저장소 내 문서(예: Wiki)를 참고하세요.
