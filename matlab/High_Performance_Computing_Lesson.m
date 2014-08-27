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
% Still to come...
%
%
