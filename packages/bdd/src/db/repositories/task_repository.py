from pony import orm


class TaskRepository:

    @staticmethod
    @orm.db_session()
    def set_trigger_constraint_on_insert(db):
        """
        Set Trigger for exclusive or between project and asset tables foreign key

        todo : see -> https://github.com/ponyorm/pony/issues/587
        """

        my_rigger = """
        CREATE OR REPLACE FUNCTION OnInsTask() RETURNS TRIGGER AS $$$$
        begin
            IF (new.shot IS NULL AND new.asset IS NULL ) THEN
                RAISE 'Shot NOR Asset is REQUIRED';
            end if;
            
            IF (new.shot IS NOT NULL AND new.asset IS NOT NULL ) THEN
                raise 'Shot NOR Asset is REQUIRED';
            end if;
            return new;
        end;
    $$$$ LANGUAGE plpgsql;
    CREATE TRIGGER TrigInsTask
    before insert or update on public.task
        for each row execute procedure OnInsTask()"""
        cursor = db.execute(my_rigger)
        # Task.select(lambda x: orm.raw_sql(myTrigger))
