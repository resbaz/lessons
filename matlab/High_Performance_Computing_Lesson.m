%% Chapter - High Performance Computing.
%
% Authors:
% Bernard Meade, Damien Irving
%
% This chapter provides an introduction to High Performance Computing (HPC) using 
% Matlab.
%
% Outline:
%
% * Introduction to HPC 
% * Multi-core CPU parallel processing using 'parfor'
% * GPU parallel processing using 'gpuArray' and 'gather'
% * Parallel programming on a cluster using the Distributed
%   Computing Server (DCS)
% * Moving beyond embarrassingly parallel problems
%
% Reference files for this chapter:
%
% * myFunction.m
% * 
%
%% Introduction to HPC
%
% Parallel programming has been important to scientific computing for decades as a way 
% to decrease program run times, making more complex analyses possible (e.g. climate 
% modelling, gene sequencing, pharmaceutical development, aircraft design). One of the 
% motivations for parallel programming has been the diminishing marginal increases in 
% single CPU performance with each new generation of Central Processing Unit (CPU). In 
% response, computer makers have introduced multi-core processors that contain more than 
% one processing core. It's not uncommon for desktop, laptop, and even tablets and smart 
% phones to have two or more CPU cores.
%
% In addition to multi-core CPUs, Graphics Processing Units (GPU) have become more powerful 
% recently (often having hundreds of parallel execution units). GPUs are increasingly being 
% used not just for drawing graphics to the screen, but for general purpose computation. GPUs 
% can even be used in conjunction with CPUs to boost parallel computing performance (this is known
% as heterogeneous computing). GPUs are best suited to applying the same computation over arrays of 
% data, while CPUs are better suited to algorithms that include conditional branches of execution 
% (e.g. different paths through the code based on if statements).
%
% Unfortunately, most computer programs cannot take advantage of performance increases offered by GPUs 
% or multi-core CPUs unless we modify these programs. In this lesson we will develop example programs 
% that use various Matlab functions to simultaneously execute tasks on a multi-core CPU, make use of a
% GPU, and run a task across multiple computers in a computing cluster. 
%
%
%% Multi-core CPU parallel processing using 'parfor'
%
% Initialize problem
iter = 50000;
sz = 55;
a = zeros(1, iter);
%
% Monte Carlo Simulation
disp('Computing...');drawnow;
tic;
parfor simNum = 1:iter
    a(simNum) = myFunction(sz);
end
toc;

% Post processing
figure;
hist(a);
%
%
%% GPU parallel processing using 'gpuArray' and 'gather'
%
% Still to come...
%
%
%% Parallel programming on a cluster using the Distributed Computing Server (DCS)
%
% For the previous CPU and GPU examples, we were limited by the number of CPUs and/or GPUs
% available on our machine. To get access to even more processing units, we'd need to
% to run our process over multiple computers at once (i.e. across a cluster). The level of 
% complexity associated with running a process across a cluster is much higher than for a single 
% computer, so Matlab have developed the Distributed Computing Service (DCS) to simplify the 
% task. 
%
% Example still to come...
%
%
%% Moving beyond embarrassingly parallel problems 
%
% The problem we've looked at so far is "embarrassingly parallel." In other words,  
% little or no effort was required to separate it into a number of parallel tasks 
% (i.e. all we had to do was change "for" to "parfor"). This is often the case where 
% there exists no dependency (or communication) between those parallel tasks. 
%
% In contrast, distributed computing problems do require communication between tasks, 
% usually via the communication of intermediate results. There is a real science behind
% distributed computing, and it typically requires a total re-think of the way your code
% and problem is structured/framed. To cut a long story short, if your problem isn't 
% embarrassingly parallel, there isn't a simple Matlab tool to help you out. You're 
% going to need professional assistance.
%
