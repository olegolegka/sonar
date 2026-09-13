local npc= workspace.Noob
local humanoid = npc.Humanoid
local pointA=workspace.part1
local pointB=workspace.part2
local pointC=workspace.part3
local pointD=workspace.part4
local pointE=workspace.part5
while true do
	humanoid:MoveTo(pointA.Position)
	humanoid.MoveToFinished:Wait()
	humanoid:MoveTo(pointB.Position)
	humanoid.MoveToFinished:Wait()
	humanoid:MoveTo(pointC.Position)
	humanoid.MoveToFinished:Wait()
	humanoid:MoveTo(pointD.Position)
	humanoid.MoveToFinished:Wait()
	humanoid:MoveTo(pointE.Position)
	humanoid.MoveToFinished:Wait()
	wait(5)
end
