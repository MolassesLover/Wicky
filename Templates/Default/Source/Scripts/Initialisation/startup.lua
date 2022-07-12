-- Check if the script is running as intended.
-- This is equivalent to:
-- if __name__=='__main__'
if pcall(getfenv, 4) then
    error("Running the startup script as a library!")
else
    print("Running the startup script as a program.")

    -- runProcess() creates a new task used by the engine. 
    runProcess(function()
        -- This will cause the function to loop infinitely.
        while true do

            print("I will be printed every frame!")

            -- update() will wait for the next frame!
            update() -- Be careful removing this.
        end
    end)
end

