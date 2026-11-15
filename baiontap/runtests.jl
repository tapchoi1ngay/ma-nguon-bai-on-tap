using Test
include("bai.jl")

@testset "Bo kiem thu 12 ca - DT075" begin
    @test bfs_chia_lop(4, [(1,2), (2,3), (3,4)], 1) == [0, 1, 2, 3]
    @test bfs_chia_lop(3, Tuple{Int,Int}[], 2) == [-1, 0, -1]
    @test bfs_chia_lop(3, [(1,2), (2,3), (3,1)], 1) == [0, 1, 1]
    @test bfs_chia_lop(6, [(1,2), (2,3), (3,4), (4,5), (5,6)], 3) == [2, 1, 0, 1, 2, 3]
    @test bfs_chia_lop(4, [(1,2)], 1) == [0, 1, -1, -1]
    @test bfs_chia_lop(1, Tuple{Int,Int}[], 1) == [0]
    @test_throws ArgumentError bfs_chia_lop(3, [(1,1), (2,3)], 1)
    @test_throws ArgumentError bfs_chia_lop(120, [(1,2)], 1)
    @test_throws ArgumentError bfs_chia_lop(0, Tuple{Int,Int}[], 1)
    @test_throws ArgumentError bfs_chia_lop(3, [(-1,2)], 1)
    @test bfs_chia_lop(3, [(1,2), (2,1), (2,3)], 1) == [0, 1, 2]
    @test bfs_chia_lop(5, [(1,2), (1,3), (2,4), (3,5)], 1) == [0, 1, 1, 2, 2]
end
println("Tat ca 12 ca kiem thu da PASS thanh cong!")
