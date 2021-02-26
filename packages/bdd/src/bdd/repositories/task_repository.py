from pony import orm
from bdd.models.task import Task

class TaskRepository:

    @staticmethod
    @orm.db_session()
    def SetTriggerConstraintOnInsert(db):
        """
        Set Trigger for exclusive or between project and asset tables foreign key

        todo : see -> https://github.com/ponyorm/pony/issues/587
        """


        myTrigger = """CREATE OR REPLACE FUNCTION OnInsTask() RETURNS TRIGGER AS $$$$
	DECLARE
		 v_shot INTEGER;
       	 v_asset INTEGER;
	begin
		IF (v_shot = NULL AND v_asset = NULL ) THEN
			raise 'Shot or Asset is REQUIRED';
		end if;
		return new;
	end;
$$$$ LANGUAGE plpgsql;
CREATE TRIGGER TrigInsTask
before insert or update on public.task
	for each row execute procedure OnInsTask()"""
        cursor = db.execute(myTrigger)
        #Task.select(lambda x: orm.raw_sql(myTrigger))
