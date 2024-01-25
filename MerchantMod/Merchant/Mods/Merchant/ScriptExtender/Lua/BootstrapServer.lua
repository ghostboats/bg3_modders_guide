
local TutorialChestSummoning_CompanionsSet = {
	["S_Player_ShadowHeart_3ed74f06-3c60-42dc-83f6-f034cb47c679"] = true,
	["S_Player_Astarion_c7c13742-bacd-460a-8f65-f864fe41f255"] = true,
	["S_Player_Gale_ad9af97d-75da-406a-ae13-7071c563f604"] = true,
	["S_Player_Wyll_c774d764-4a17-48dc-b470-32ace9ce447d"] = true,
	["S_Player_Karlach_2c76687d-93a2-477b-8b18-8a14b549304c"] = true,
	["S_Player_Laezel_58a69333-40bf-8358-1d17-fff240d7fb12"] = true,
	["S_Player_Jaheira_91b6b200-7d00-4d62-8dc9-99e8339dfa1a"] = true,
	["S_Player_Minsc_0de603c5-42e2-4811-9dad-f652de080eba"] = true,

	["S_GLO_Halsin_7628bc0e-52b8-42a7-856a-13a6fd413323"] = true,
	["S_GOB_DrowCommander_25721313-0c15-4935-8176-9f134385451b"] = true,
}

local function TutorialChestSummoning_ShouldHaveSpell(uuid)
	if Osi.IsTagged(uuid, "306b9b05-1057-4770-aa17-01af21acd650") == 1 -- AVATAR
	or TutorialChestSummoning_CompanionsSet[uuid]
	then
		return true
	end

	local hirelingMatches = Osi.DB_Hirelings_Hired:Get(uuid)
	return #hirelingMatches > 0
end

local function TutorialChestSummoning_GetPartyMembers()
	local partyMembersDB = Osi.DB_PartyMembers:Get(nil)

	local partyMembersSet = {}
	for _, v in pairs(partyMembersDB) do
		local uuid = v[1]
		-- print("DB_PartyMembers: " .. uuid)
		partyMembersSet[uuid] = true
	end
	return partyMembersSet
end

local function TutorialChestSummoning_GetPartOfTheTeam()
	local partOfTheTeamDB = Osi.DB_PartOfTheTeam:Get(nil)

	local partOfTheTeamSet = {}
	for _, v in pairs(partOfTheTeamDB) do
		local uuid = v[1]
		-- print("DB_PartOfTheTeam: " .. uuid)
		partOfTheTeamSet[uuid] = true
	end
	return partOfTheTeamSet
end

local function TutorialChestSummoning_CharacterJoinedParty_Apply(character)
	-- print("TutorialChestSummoning: CharacterJoinedParty: " .. character)

	if Osi.HasActiveStatus(character, "TCP_BOOST_DRANKPOTION") == 0
	and TutorialChestSummoning_ShouldHaveSpell(character)
	then
		print("TutorialChestSummoning: Applying to " .. character)
		Osi.ApplyStatus(character, "TCP_BOOST_DRANKPOTION_APPLY", 0)
	end
end

local function TutorialChestSummoning_DB_PartOfTheTeam_afterDelete(character)
	-- print("TutorialChestSummoning: DB_PartOfTheTeam afterDelete: " .. character)

	if Osi.HasActiveStatus(character, "TCP_BOOST_DRANKPOTION") == 1	then
		print("TutorialChestSummoning: Removing from " .. character)
		Osi.RemoveStatus(character, "TCP_BOOST_DRANKPOTION")
	end
end

local function TutorialChestSummoning_OnGameStateChanged_Apply(event)
	-- print("TutorialChestSummoning: GameStateChanged: " .. event.FromState.Label .. " -> " .. event.ToState.Label)

	if event.FromState ~= "Sync" or event.ToState ~= "Running" then
		return
	end

	local partyMembersSet = TutorialChestSummoning_GetPartyMembers()
	local partOfTheTeamSet = TutorialChestSummoning_GetPartOfTheTeam()

	local charsToApplyTo = {}
	local applyCount = 0
	for uuid, _ in pairs(partyMembersSet) do
		if partOfTheTeamSet[uuid] then
			if TutorialChestSummoning_ShouldHaveSpell(uuid) then
				if Osi.HasActiveStatus(uuid, "TCP_BOOST_DRANKPOTION") == 0 then
					charsToApplyTo[uuid] = true
					applyCount = applyCount + 1
				end
			end
		end
	end

	print("TutorialChestSummoning: Applying status to " .. applyCount .. " characters")
	for uuid, _ in pairs(charsToApplyTo) do
		print("TutorialChestSummoning: Applying to " .. uuid)
		Osi.ApplyStatus(uuid, "TCP_BOOST_DRANKPOTION_APPLY", 0)
	end
end

local function TutorialChestSummoning_CharacterLeftParty_Remove(character)
	-- print("TutorialChestSummoning: CharacterLeftParty: " .. character)

	if Osi.HasActiveStatus(character, "TCP_BOOST_DRANKPOTION") == 1 then
		print("TutorialChestSummoning: Removing from " .. character)
		Osi.RemoveStatus(character, "TCP_BOOST_DRANKPOTION")
	end
end

local function TutorialChestSummoning_OnGameStateChanged_Remove(event)
	-- print("TutorialChestSummoning: GameStateChanged: " .. event.FromState.Label .. " -> " .. event.ToState.Label)

	if event.FromState ~= "Sync" or event.ToState ~= "Running" then
		return
	end

	local partyMembersSet = TutorialChestSummoning_GetPartyMembers()
	local partOfTheTeamSet = TutorialChestSummoning_GetPartOfTheTeam()

	local charsToRemoveFrom = {}
	local removeCount = 0
	for uuid, _ in pairs(partyMembersSet) do
		if Osi.HasActiveStatus(uuid, "TCP_BOOST_DRANKPOTION") == 1 then
			charsToRemoveFrom[uuid] = true
			removeCount = removeCount + 1
		end
	end
	for uuid, _ in pairs(partOfTheTeamSet) do
		if not charsToRemoveFrom[uuid] then
			if Osi.HasActiveStatus(uuid, "TCP_BOOST_DRANKPOTION") == 1 then
				charsToRemoveFrom[uuid] = true
				removeCount = removeCount + 1
			end
		end
	end
	for uuid, _ in pairs(TutorialChestSummoning_CompanionsSet) do
		if not charsToRemoveFrom[uuid] then
			if Osi.HasActiveStatus(uuid, "TCP_BOOST_DRANKPOTION") == 1 then
				charsToRemoveFrom[uuid] = true
				removeCount = removeCount + 1
			end
		end
	end

	print("TutorialChestSummoning: Removing status from " .. removeCount .. " characters")
	for uuid, _ in pairs(charsToRemoveFrom) do
		print("TutorialChestSummoning: Removing from " .. uuid)
		Osi.RemoveStatus(uuid, "TCP_BOOST_DRANKPOTION")
	end
end

if true then
	Ext.Osiris.RegisterListener("CharacterJoinedParty", 1, "after", TutorialChestSummoning_CharacterJoinedParty_Apply)
	Ext.Osiris.RegisterListener("DB_PartOfTheTeam", 1, "afterDelete", TutorialChestSummoning_DB_PartOfTheTeam_afterDelete)
	Ext.Events.GameStateChanged:Subscribe(TutorialChestSummoning_OnGameStateChanged_Apply)
else
	Ext.Osiris.RegisterListener("CharacterLeftParty", 1, "after", TutorialChestSummoning_CharacterLeftParty_Remove)
	Ext.Events.GameStateChanged:Subscribe(TutorialChestSummoning_OnGameStateChanged_Remove)
end
