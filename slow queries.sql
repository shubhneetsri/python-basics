# Query_time : 48.379732
SELECT SQL_CALC_FOUND_ROWS 
                IF(attachment_id, 1, 0) AS attachmentPresent,
                company.is_hot AS isHot,
                company.company_id AS companyID,
                company.company_id AS exportID,
                company.is_hot AS isHot,
                company.date_modified AS dateModifiedSort,
                company.date_created AS dateCreatedSort,
            IF(attachment_id, 1, 0) AS attachmentPresent,
company.name AS name,
(
                                                            SELECT
                                                                COUNT(*)
                                                            FROM
                                                                joborder
                                                            WHERE
                                                                company_id = company.company_id
                                                            AND
                                                                site_id = 1
                                                        ) AS jobs,
company.city AS city,
company.state AS state,
company.phone1 AS phone,
owner_user.first_name AS ownerFirstName,owner_user.last_name AS ownerLastName,CONCAT(owner_user.last_name, owner_user.first_name) AS ownerSort,
DATE_FORMAT(company.date_created, '%m-%d-%y') AS dateCreated,
DATE_FORMAT(company.date_modified, '%m-%d-%y') AS dateModified
            FROM
                company
            LEFT JOIN user AS owner_user
                ON company.owner = owner_user.user_id
            LEFT JOIN joborder
                ON company.company_id = joborder.company_id
            LEFT JOIN contact
                ON company.billing_contact = contact.contact_id
            LEFT JOIN attachment
                ON company.company_id = attachment.data_item_id
                AND attachment.data_item_type = 200
             LEFT JOIN saved_list_entry
                                    ON saved_list_entry.data_item_type = 200
                                    AND saved_list_entry.data_item_id = company.company_id
                                    AND saved_list_entry.site_id = 1
            WHERE
                company.site_id = 1
            
            
            GROUP BY company.company_id
            
            ORDER BY dateCreatedSort DESC
            LIMIT 0, 15;

# Query_time : 32.005715

SELECT SQL_CALC_FOUND_ROWS 
                                        joborder.joborder_id AS jobOrderID,
                                        joborder.joborder_id AS exportID,
                                        joborder.date_modified AS dateModifiedSort,
                                        joborder.date_created AS dateCreatedSort,
                                        joborder.sla_date AS dateSlaSort,
                                        joborder.approved_date AS dateApprovedSort,
                                        joborder.is_hot AS isHot,
                                        IF(attachment_id, 1, 0) AS attachmentPresent,
joborder.title AS title,
joborder.status AS status,
DATE_FORMAT(joborder.date_created, '%m-%d-%y') AS dateCreated,
DATEDIFF(NOW(), joborder.approved_date) AS daysOld,
(
SELECT
COUNT(*)
FROM
candidate_joborder_status_history
WHERE
joborder_id = joborder.joborder_id
AND
status_to = 400
AND
site_id = 1
) AS submitted,
(
SELECT
COUNT(*)
FROM
candidate_joborder
WHERE
joborder_id = joborder.joborder_id
AND
site_id = 1
) AS pipeline,
recruiter_user.first_name AS recruiterFirstName,recruiter_user.last_name AS recruiterLastName,CONCAT(recruiter_user.last_name, recruiter_user.first_name) AS recruiterSort,
owner_user.first_name AS ownerFirstName,owner_user.last_name AS ownerLastName,CONCAT(owner_user.last_name, owner_user.first_name) AS ownerSort,
department.duname AS du,
joborderpriority.priorityname AS priorityname
                                        FROM
                                        joborder
                                        LEFT JOIN company
                                        ON joborder.company_id = company.company_id
                                        LEFT JOIN contact
                                        ON joborder.contact_id = contact.contact_id
                                        LEFT JOIN attachment
                                        ON joborder.joborder_id = attachment.data_item_id
                                        AND attachment.data_item_type = 400
                                        LEFT JOIN user AS recruiter_user ON joborder.recruiter = recruiter_user.user_id
LEFT JOIN user AS owner_user ON joborder.owner = owner_user.user_id
LEFT JOIN department ON department.duid = joborder.bu
LEFT JOIN joborderpriority ON joborderpriority.joborder_id = joborder.joborder_id LEFT JOIN saved_list_entry
                        ON saved_list_entry.data_item_type = 400
                        AND saved_list_entry.data_item_id = joborder.joborder_id
                        AND saved_list_entry.site_id = 1
                                        WHERE
                                        joborder.site_id = 1

                                        AND joborder.is_admin_hidden = 0
                                        
                                        
                                        AND joborder.approvalstatus in(0,1)
                                        AND joborder.bu != 11                        
                                        GROUP BY joborder.joborder_id
                                        
                                        ORDER BY dateCreatedSort DESC
                                        LIMIT 0, 50;

# Query_time : 29.920292

SELECT SQL_CALC_FOUND_ROWS 
                candidate.candidate_id AS candidateID,
                candidate.candidate_id AS exportID,
                candidate.is_hot AS isHot,
                candidate.date_modified AS dateModifiedSort,
                candidate.date_created AS dateCreatedSort,
            IF(candidate_joborder_submitted.candidate_joborder_id, 1, 0) AS submitted,
                                                IF(attachment_id, 1, 0) AS attachmentPresent,
candidate.first_name AS firstName,
candidate.last_name AS lastName,
candidate.city AS city,
candidate.state AS state,
candidate.key_skills AS keySkills,
owner_user.first_name AS ownerFirstName,owner_user.last_name AS ownerLastName,CONCAT(owner_user.last_name, owner_user.first_name) AS ownerSort,
DATE_FORMAT(candidate.date_created, '%m-%d-%y') AS dateCreated,
DATE_FORMAT(candidate.date_modified, '%m-%d-%y') AS dateModified
            FROM
                candidate
            LEFT JOIN attachment
                                                        ON candidate.candidate_id = attachment.data_item_id
                                                                                                                AND attachment.data_item_type = 100
                                                    LEFT JOIN candidate_joborder AS candidate_joborder_submitted
                                                        ON candidate_joborder_submitted.candidate_id = candidate.candidate_id
                                                        AND candidate_joborder_submitted.status >= 400
                                                        AND candidate_joborder_submitted.site_id = 1
                                                        AND candidate_joborder_submitted.status != 650
LEFT JOIN user AS owner_user ON candidate.owner = owner_user.user_id LEFT JOIN saved_list_entry
                                    ON saved_list_entry.data_item_type = 100
                                    AND saved_list_entry.data_item_id = candidate.candidate_id
                                    AND saved_list_entry.site_id = 1
            WHERE
                candidate.site_id = 1
            AND candidate.is_admin_hidden = 0
            
             AND candidate.owner = 2181 GROUP BY candidate.candidate_id
            
            ORDER BY dateModifiedSort DESC
            LIMIT 0, 15;

# Query_time : 27.079883

SELECT CONCAT(us.first_name, ' ', us.last_name) as "owner",CONCAT(uss.first_name, ' ', uss.last_name) as "mentor",CONCAT(usss.first_name, ' ', usss.last_name) as "duheadname",jo.title,cjop.joborder_id ,can.candidate_id,CONCAT(can.first_name,' ',can.last_name) as "candidatename",CONCAT(ussss.first_name, ' ', ussss.last_name) as "recruiter",jo.recruiter as recruiterId, joining_date,key_skills,jo.skill,deg.designation,grp.groupname,rol.rolename,du.duname,canjs.short_description,codp.name,jo.type,dobDate,levelgrades,gender,can.location,jo.gradelevel FROM `candidate` can LEFT JOIN candidate_joborder cjop ON cjop.candidate_id=can.candidate_id LEFT JOIN joborder jo on jo.joborder_id=cjop.joborder_id LEFT JOIN user us on us.user_id=jo.owner LEFT JOIN user uss on uss.user_id=jo.mentor LEFT JOIN tbldesignation deg on deg.designationid=can.designation LEFT JOIN tblgroup grp on grp.groupid=can.usergroup LEFT JOIN tblroles rol on rol.roleid=can.role LEFT JOIN department du on du.duid=jo.bu LEFT JOIN tbldu tbldu ON tbldu.duid = du.duid LEFT JOIN user ussss on ussss.user_id=jo.recruiter LEFT JOIN user usss ON (usss.user_id = tbldu.duheadusrid1 OR usss.user_id = tbldu.duheadusrid2) LEFT JOIN candidate_joborder_status canjs on canjs.candidate_joborder_status_id=cjop.status LEFT JOIN company_department codp on codp.company_department_id=jo.company_department_id WHERE can.joining_date >='2025-07-07 23:59:59' and cjop.status in (915) and du.duid IN(1,5,13,14,15,16,19,21,24,25,26) order by canjs.short_description;

# Query_time : 3.64836

SELECT Concat(can.first_name, ' ', can.last_name) AS candidateFullName,
            Datediff(us.resigndate, us.doj)            AS datediff,
            can.candidate_id,
            can.key_skills,
            can.ispaid,
            canjo.status,
            us.doj,
            us.resigndate,
            canjo.joborder_id,
            jo.title,
            jo.city AS location,
            canjo.date_created,
            canjs.short_description,
            act.notes AS notes,
            cal_event.feedback AS feedback,
            bamu.bonusamount
            FROM   candidate can
                LEFT JOIN candidate_joborder canjo
                        ON canjo.candidate_id = can.candidate_id
                LEFT JOIN joborder jo
                        ON canjo.joborder_id = jo.joborder_id
                LEFT JOIN candidate_joborder_status canjs
                        ON canjs.candidate_joborder_status_id = canjo.status
                LEFT JOIN tblbonusamount bamu
                        ON bamu.level = can.levelgrades
                LEFT JOIN user us
                        ON us.candidate_id = can.candidate_id
                LEFT JOIN (
                    SELECT 
                        data_item_id,
                        GROUP_CONCAT(feedback SEPARATOR ', ') AS feedback
                    FROM 
                        calendar_event
                    GROUP BY 
                        data_item_id
                ) cal_event
                ON 
                    can.candidate_id = cal_event.data_item_id
                LEFT JOIN (
                    SELECT a.data_item_id, a.notes
                    FROM activity a
                    INNER JOIN (
                        SELECT data_item_id, MAX(activity_id) AS latest_activity_id
                        FROM activity
                        WHERE data_item_id IS NOT NULL
                        GROUP BY data_item_id
                    ) latest_act
                    ON a.data_item_id = latest_act.data_item_id
                    AND a.activity_id = latest_act.latest_activity_id
                ) act
                ON can.candidate_id = act.data_item_id
            WHERE  can.entered_by = 1917
                AND canjo.status != 885
                AND (
                    can.candidate_id IN (
                        SELECT candidate_id
                        FROM candidate_joborder
                        WHERE candidate_id IN (
                            SELECT candidate_id
                            FROM candidate
                            WHERE isreferral = 2
                                    AND entered_by = 1917
                        )
                        AND candidate_joborder.status != 885
                    )
                    OR can.candidate_id IN (
                        SELECT candidate_id
                        FROM candidate
                        WHERE candidate_id NOT IN (
                            SELECT candidate_id
                            FROM candidate_joborder
                            WHERE candidate_id IN (
                                SELECT candidate_id
                                FROM candidate
                                WHERE isreferral = 2
                                        AND entered_by = 1917
                            )
                        )
                        AND isreferral = 2
                        AND entered_by = 1917
                    )
                    );