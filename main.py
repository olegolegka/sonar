local event = game.ReplicatedStorage.ShootEvent
local bullet = game.ReplicatedStorage.Bullet
local speed = 50
local debris = game:GetService("Debris")

event.OnServerEvent:Connect(function(player,mousepos,muzzelpos)
	local bulletclone = bullet:Clone()
	bulletclone.Parent = workspace
	bulletclone.CFrame = CFrame.lookAt(muzzelpos,mousepos)
	local direction = (mousepos - muzzelpos).Unit
	local velocity = bulletclone.LinearVelocity
	velocity.VectorVelocity = direction * speed
	bulletclone.Touched:Connect(function(hit)
		if hit.Parent:FindFirstChild("Humanoid") then
			hit.Parent:FindFirstChild("Humanoid"):TakeDamage(25)
		end
		bulletclone:Destroy()
	end)
	debris:AddItem(bulletclone,5)
end)
