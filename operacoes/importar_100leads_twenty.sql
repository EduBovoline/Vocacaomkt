
    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c09f9ac9-179b-493e-8faf-5a09da1c27b4', NOW(), NOW(), 'Silvério Odontologia', 'Av. Pereira da Silva, 169',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '276f5501-7954-4c5b-a172-6dd99fdcb87a', NOW(), NOW(), 'Responsável Comercial', 'Silvério Odontologia',
        '551530165548', 'c09f9ac9-179b-493e-8faf-5a09da1c27b4', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8f3d171a-6802-4f96-98ad-b7b500f9fbe1', NOW(), NOW(), 'Silvério Odontologia — Vocação Update (Reforma Mobile-First)', 'NEW', 980000000, 'BRL',
        'c09f9ac9-179b-493e-8faf-5a09da1c27b4', '276f5501-7954-4c5b-a172-6dd99fdcb87a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8238c5d1-5f7c-4457-a58d-d6b256a3f1de', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 169)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Update (Reforma Mobile-First)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 80%\n- **Telefone:** 551530165548',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '8238c5d1-5f7c-4457-a58d-d6b256a3f1de', 'c09f9ac9-179b-493e-8faf-5a09da1c27b4', '276f5501-7954-4c5b-a172-6dd99fdcb87a', '8f3d171a-6802-4f96-98ad-b7b500f9fbe1',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a5d79a55-9d7f-4d4d-898b-f84772a79dc0', NOW(), NOW(), 'Orodent Unidade Santa Rosália', 'Av. Pereira da Silva, 1631',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '03ff4e57-f61b-43e0-816a-bf5c6be9d65c', NOW(), NOW(), 'Responsável Comercial', 'Orodent Unidade Santa Rosália',
        '551533571363', 'a5d79a55-9d7f-4d4d-898b-f84772a79dc0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '42972a43-a0f8-4ae2-b0d3-87d67e8709a9', NOW(), NOW(), 'Orodent Unidade Santa Rosália — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'a5d79a55-9d7f-4d4d-898b-f84772a79dc0', '03ff4e57-f61b-43e0-816a-bf5c6be9d65c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3a407260-32b7-4b51-91b7-7648e038a34d', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1631)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551533571363',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '3a407260-32b7-4b51-91b7-7648e038a34d', 'a5d79a55-9d7f-4d4d-898b-f84772a79dc0', '03ff4e57-f61b-43e0-816a-bf5c6be9d65c', '42972a43-a0f8-4ae2-b0d3-87d67e8709a9',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7784091b-5cbf-45e3-9af3-68f750dceb2d', NOW(), NOW(), 'Clínica Russo Odontologia', 'Av. Pereira da Silva, 127',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f3f3e218-4811-49e3-8bd6-ca82aa69783d', NOW(), NOW(), 'Responsável Comercial', 'Clínica Russo Odontologia',
        '551532331516', '7784091b-5cbf-45e3-9af3-68f750dceb2d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e6a2336e-b8a8-4833-8fda-fcde24100f03', NOW(), NOW(), 'Clínica Russo Odontologia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '7784091b-5cbf-45e3-9af3-68f750dceb2d', 'f3f3e218-4811-49e3-8bd6-ca82aa69783d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9111404e-0951-459c-87e0-97690b1350b9', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 127)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532331516',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9111404e-0951-459c-87e0-97690b1350b9', '7784091b-5cbf-45e3-9af3-68f750dceb2d', 'f3f3e218-4811-49e3-8bd6-ca82aa69783d', 'e6a2336e-b8a8-4833-8fda-fcde24100f03',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '169c6fe5-1230-403a-ab92-d0e245d58fbd', NOW(), NOW(), 'Dr. Gaspar Martins da Silva', 'Av. Pereira da Silva, 1175',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e90af0e1-0d4b-4ce7-a417-30b8b3bfc3f5', NOW(), NOW(), 'Responsável Comercial', 'Dr. Gaspar Martins da Silva',
        '551532310205', '169c6fe5-1230-403a-ab92-d0e245d58fbd', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6f1a4e87-e1c7-484e-8ce1-988a7e14e92f', NOW(), NOW(), 'Dr. Gaspar Martins da Silva — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '169c6fe5-1230-403a-ab92-d0e245d58fbd', 'e90af0e1-0d4b-4ce7-a417-30b8b3bfc3f5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8c0426b0-3601-4bef-b338-4a1a7b865c4e', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1175)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532310205',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '8c0426b0-3601-4bef-b338-4a1a7b865c4e', '169c6fe5-1230-403a-ab92-d0e245d58fbd', 'e90af0e1-0d4b-4ce7-a417-30b8b3bfc3f5', '6f1a4e87-e1c7-484e-8ce1-988a7e14e92f',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '98386bb9-f489-4ff5-9e3c-f44df34c4d20', NOW(), NOW(), 'RP Prime Odontologia', 'Av. Pereira da Silva, 56',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0069de79-2f62-40b9-be3d-f049f372a4dd', NOW(), NOW(), 'Responsável Comercial', 'RP Prime Odontologia',
        '551530111204', '98386bb9-f489-4ff5-9e3c-f44df34c4d20', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'fc9028c8-c5d8-4930-b0ec-7b4ade3561cb', NOW(), NOW(), 'RP Prime Odontologia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '98386bb9-f489-4ff5-9e3c-f44df34c4d20', '0069de79-2f62-40b9-be3d-f049f372a4dd', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3d7952c9-b7d7-4d10-abd7-f6c49b4143ee', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 56)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551530111204',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '3d7952c9-b7d7-4d10-abd7-f6c49b4143ee', '98386bb9-f489-4ff5-9e3c-f44df34c4d20', '0069de79-2f62-40b9-be3d-f049f372a4dd', 'fc9028c8-c5d8-4930-b0ec-7b4ade3561cb',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'acf4f09a-5328-4d5f-9984-90717c1590d6', NOW(), NOW(), 'Clínica Vanessa Nogueira Emagrecimento', 'Av. Pereira da Silva, 1099',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '60b6969a-63f4-4fef-94c8-e2215c1f499e', NOW(), NOW(), 'Responsável Comercial', 'Clínica Vanessa Nogueira Emagrecimento',
        '551530313394', 'acf4f09a-5328-4d5f-9984-90717c1590d6', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '345347f1-5169-4e95-901e-13e54e08ad00', NOW(), NOW(), 'Clínica Vanessa Nogueira Emagrecimento — Vocação Update (Reforma Mobile-First)', 'NEW', 980000000, 'BRL',
        'acf4f09a-5328-4d5f-9984-90717c1590d6', '60b6969a-63f4-4fef-94c8-e2215c1f499e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ae80d4d0-b053-4c8e-aff9-561f358fa9ca', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1099)\n**Categoria:** Saúde & Estética\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Update (Reforma Mobile-First)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 80%\n- **Telefone:** 551530313394',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ae80d4d0-b053-4c8e-aff9-561f358fa9ca', 'acf4f09a-5328-4d5f-9984-90717c1590d6', '60b6969a-63f4-4fef-94c8-e2215c1f499e', '345347f1-5169-4e95-901e-13e54e08ad00',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c650e54b-aaa5-4898-a650-947772a7241d', NOW(), NOW(), 'Clínica Equilíbrio Saúde', 'Av. Pereira da Silva, 828',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f8845850-ee59-4f65-aed9-60a9dc4b82b5', NOW(), NOW(), 'Responsável Comercial', 'Clínica Equilíbrio Saúde',
        '551532348890', 'c650e54b-aaa5-4898-a650-947772a7241d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3d4dc5a9-8246-46a7-b4ed-8a3d2f5f1136', NOW(), NOW(), 'Clínica Equilíbrio Saúde — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'c650e54b-aaa5-4898-a650-947772a7241d', 'f8845850-ee59-4f65-aed9-60a9dc4b82b5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '06683251-0e81-40c4-b87c-90e8d050b148', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 828)\n**Categoria:** Saúde Multidisciplinar\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532348890',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '06683251-0e81-40c4-b87c-90e8d050b148', 'c650e54b-aaa5-4898-a650-947772a7241d', 'f8845850-ee59-4f65-aed9-60a9dc4b82b5', '3d4dc5a9-8246-46a7-b4ed-8a3d2f5f1136',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bdfffeca-e67b-4d76-b3f2-a971e1eda9c0', NOW(), NOW(), 'Clínica LES Medicina e Reabilitação', 'R. Maria Cinto de Biaggi, 125',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '744ed6a2-247e-480a-8fcb-4d55836a9357', NOW(), NOW(), 'Responsável Comercial', 'Clínica LES Medicina e Reabilitação',
        '551532335772', 'bdfffeca-e67b-4d76-b3f2-a971e1eda9c0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c4ac7518-ad40-4f9e-beae-1c6f48ab3d10', NOW(), NOW(), 'Clínica LES Medicina e Reabilitação — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        'bdfffeca-e67b-4d76-b3f2-a971e1eda9c0', '744ed6a2-247e-480a-8fcb-4d55836a9357', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a1f73d40-668d-4ef6-a971-58ec9a79ae7b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Maria Cinto de Biaggi, 125)\n**Categoria:** Clínica Médica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532335772',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'a1f73d40-668d-4ef6-a971-58ec9a79ae7b', 'bdfffeca-e67b-4d76-b3f2-a971e1eda9c0', '744ed6a2-247e-480a-8fcb-4d55836a9357', 'c4ac7518-ad40-4f9e-beae-1c6f48ab3d10',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '322bbd17-159a-4e09-8e5d-9415ed5ea895', NOW(), NOW(), 'CeiPre Saúde & Fisioterapia', 'R. João dos Santos, 600',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '25bc149c-5fbf-435e-8f87-45e95e873f49', NOW(), NOW(), 'Responsável Comercial', 'CeiPre Saúde & Fisioterapia',
        '551534188848', '322bbd17-159a-4e09-8e5d-9415ed5ea895', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd1cb4a9a-6653-4410-a39a-aa75c2ab4caf', NOW(), NOW(), 'CeiPre Saúde & Fisioterapia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '322bbd17-159a-4e09-8e5d-9415ed5ea895', '25bc149c-5fbf-435e-8f87-45e95e873f49', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cc77de2f-60f1-4367-83aa-bfc26d0d7dad', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. João dos Santos, 600)\n**Categoria:** Fisioterapia & Saúde\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551534188848',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'cc77de2f-60f1-4367-83aa-bfc26d0d7dad', '322bbd17-159a-4e09-8e5d-9415ed5ea895', '25bc149c-5fbf-435e-8f87-45e95e873f49', 'd1cb4a9a-6653-4410-a39a-aa75c2ab4caf',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd58304f4-b7b4-486f-ad95-20349fe5082e', NOW(), NOW(), 'Fisio Santa Rosália', 'R. Rev. Henrique de Oliveira Camargo, 411',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '295eedc2-97d0-4f75-afc8-049c4e78d969', NOW(), NOW(), 'Responsável Comercial', 'Fisio Santa Rosália',
        '551532321450', 'd58304f4-b7b4-486f-ad95-20349fe5082e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '466ac605-1532-486a-96c8-1701447827e1', NOW(), NOW(), 'Fisio Santa Rosália — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'd58304f4-b7b4-486f-ad95-20349fe5082e', '295eedc2-97d0-4f75-afc8-049c4e78d969', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '763287a7-7e90-4573-8462-bb6c1313ff4a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Rev. Henrique de Oliveira Camargo, 411)\n**Categoria:** Fisioterapia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532321450',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '763287a7-7e90-4573-8462-bb6c1313ff4a', 'd58304f4-b7b4-486f-ad95-20349fe5082e', '295eedc2-97d0-4f75-afc8-049c4e78d969', '466ac605-1532-486a-96c8-1701447827e1',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5b985fad-5358-4c94-bc03-0c8efb7da04e', NOW(), NOW(), 'Consultório Pediátrico Santa Rosália', 'R. Mascarenhas Camelo, 310',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'dc2d38c3-8c1b-43eb-b4c7-0268464b7ecd', NOW(), NOW(), 'Responsável Comercial', 'Consultório Pediátrico Santa Rosália',
        '551532314560', '5b985fad-5358-4c94-bc03-0c8efb7da04e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '61b86cdd-7e32-4ab2-a10e-db46df613b0a', NOW(), NOW(), 'Consultório Pediátrico Santa Rosália — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '5b985fad-5358-4c94-bc03-0c8efb7da04e', 'dc2d38c3-8c1b-43eb-b4c7-0268464b7ecd', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bfd844d3-73a7-4704-ad08-372d09790611', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 310)\n**Categoria:** Pediatria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532314560',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'bfd844d3-73a7-4704-ad08-372d09790611', '5b985fad-5358-4c94-bc03-0c8efb7da04e', 'dc2d38c3-8c1b-43eb-b4c7-0268464b7ecd', '61b86cdd-7e32-4ab2-a10e-db46df613b0a',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9d300049-15c4-4e7c-b0b0-2c5c94ea3de1', NOW(), NOW(), 'Clínica de Psicologia & Terapias Rosália', 'R. Nicolau Alonso Filho, 88',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ff40a2ac-0142-42c5-81d8-715485671513', NOW(), NOW(), 'Responsável Comercial', 'Clínica de Psicologia & Terapias Rosália',
        '5515998124010', '9d300049-15c4-4e7c-b0b0-2c5c94ea3de1', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'eb6f1673-b612-4bb5-bd27-19fd72e03c6e', NOW(), NOW(), 'Clínica de Psicologia & Terapias Rosália — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '9d300049-15c4-4e7c-b0b0-2c5c94ea3de1', 'ff40a2ac-0142-42c5-81d8-715485671513', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7de604ff-4664-4a1a-b976-c4c4dbd32824', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Nicolau Alonso Filho, 88)\n**Categoria:** Psicologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515998124010',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '7de604ff-4664-4a1a-b976-c4c4dbd32824', '9d300049-15c4-4e7c-b0b0-2c5c94ea3de1', 'ff40a2ac-0142-42c5-81d8-715485671513', 'eb6f1673-b612-4bb5-bd27-19fd72e03c6e',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5171acb1-aec2-48c8-94e8-1e2b1f5bf322', NOW(), NOW(), 'Espaço Reab Postural & RPG', 'Av. Pereira da Silva, 430',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '371b383e-7112-48de-b8af-8a259e2b77f7', NOW(), NOW(), 'Responsável Comercial', 'Espaço Reab Postural & RPG',
        '5515997812030', '5171acb1-aec2-48c8-94e8-1e2b1f5bf322', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bbee5504-03d7-4802-ba55-598c8b9d38c8', NOW(), NOW(), 'Espaço Reab Postural & RPG — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '5171acb1-aec2-48c8-94e8-1e2b1f5bf322', '371b383e-7112-48de-b8af-8a259e2b77f7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd3979a71-dff2-4006-9817-a2efc81bb8c3', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 430)\n**Categoria:** Fisioterapia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515997812030',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'd3979a71-dff2-4006-9817-a2efc81bb8c3', '5171acb1-aec2-48c8-94e8-1e2b1f5bf322', '371b383e-7112-48de-b8af-8a259e2b77f7', 'bbee5504-03d7-4802-ba55-598c8b9d38c8',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd01323ac-fa12-4e67-ab44-017a95271615', NOW(), NOW(), 'Consultório de Fonoaudiologia Integrada', 'R. Mascarenhas Camelo, 190',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '047e422f-6343-4fa7-98b0-e74a775ed17b', NOW(), NOW(), 'Responsável Comercial', 'Consultório de Fonoaudiologia Integrada',
        '551532349010', 'd01323ac-fa12-4e67-ab44-017a95271615', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd1c129a0-c8f2-4259-bdcf-439833e6099b', NOW(), NOW(), 'Consultório de Fonoaudiologia Integrada — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'd01323ac-fa12-4e67-ab44-017a95271615', '047e422f-6343-4fa7-98b0-e74a775ed17b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cc86511a-75c7-4114-a04a-77566bb7268c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 190)\n**Categoria:** Fonoaudiologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532349010',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'cc86511a-75c7-4114-a04a-77566bb7268c', 'd01323ac-fa12-4e67-ab44-017a95271615', '047e422f-6343-4fa7-98b0-e74a775ed17b', 'd1c129a0-c8f2-4259-bdcf-439833e6099b',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '63034222-0314-4e95-96e4-83be4c4c5f32', NOW(), NOW(), 'Clínica Dermatológica Dra. Paula', 'Av. Pereira da Silva, 920',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '59e2830a-1305-4189-b125-cd8440708754', NOW(), NOW(), 'Responsável Comercial', 'Clínica Dermatológica Dra. Paula',
        '5515996145520', '63034222-0314-4e95-96e4-83be4c4c5f32', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1352e8a3-1221-4e5e-94f2-ea49d5133577', NOW(), NOW(), 'Clínica Dermatológica Dra. Paula — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '63034222-0314-4e95-96e4-83be4c4c5f32', '59e2830a-1305-4189-b125-cd8440708754', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1f203474-9454-42f7-8027-77c8b61f4130', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 920)\n**Categoria:** Dermatologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515996145520',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1f203474-9454-42f7-8027-77c8b61f4130', '63034222-0314-4e95-96e4-83be4c4c5f32', '59e2830a-1305-4189-b125-cd8440708754', '1352e8a3-1221-4e5e-94f2-ea49d5133577',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '626849ef-9ddc-43ac-96fe-54b5fd58bb03', NOW(), NOW(), 'Clínica Paes Pilates & Fisio', 'Av. Pereira da Silva, 164',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd4cb6bb6-f2b5-4571-bf55-db55fd7a22b2', NOW(), NOW(), 'Responsável Comercial', 'Clínica Paes Pilates & Fisio',
        '5515991767971', '626849ef-9ddc-43ac-96fe-54b5fd58bb03', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'fa60e912-ca16-496e-ae5a-3854d3593ac3', NOW(), NOW(), 'Clínica Paes Pilates & Fisio — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '626849ef-9ddc-43ac-96fe-54b5fd58bb03', 'd4cb6bb6-f2b5-4571-bf55-db55fd7a22b2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '14354887-6089-4bd9-93e8-f4e5525bc0ff', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 164)\n**Categoria:** Pilates\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515991767971',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '14354887-6089-4bd9-93e8-f4e5525bc0ff', '626849ef-9ddc-43ac-96fe-54b5fd58bb03', 'd4cb6bb6-f2b5-4571-bf55-db55fd7a22b2', 'fa60e912-ca16-496e-ae5a-3854d3593ac3',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '690fe6aa-0136-438b-be3e-6494e7559641', NOW(), NOW(), 'Sem Limites Studio Pilates', 'R. Nicolau Alonso Filho, 215',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0c18d29b-7805-4c7c-ab74-c9c43e0cbecc', NOW(), NOW(), 'Responsável Comercial', 'Sem Limites Studio Pilates',
        '5515997230411', '690fe6aa-0136-438b-be3e-6494e7559641', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c2e26a23-4522-4d56-aaed-dc927a6bde91', NOW(), NOW(), 'Sem Limites Studio Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '690fe6aa-0136-438b-be3e-6494e7559641', '0c18d29b-7805-4c7c-ab74-c9c43e0cbecc', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3672f202-6d9f-4908-bbb8-c1942276114a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Nicolau Alonso Filho, 215)\n**Categoria:** Pilates\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515997230411',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '3672f202-6d9f-4908-bbb8-c1942276114a', '690fe6aa-0136-438b-be3e-6494e7559641', '0c18d29b-7805-4c7c-ab74-c9c43e0cbecc', 'c2e26a23-4522-4d56-aaed-dc927a6bde91',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ed73c9e1-e24a-4da8-b63b-3cb2a0965b40', NOW(), NOW(), 'Pure Pilates Santa Rosália', 'R. Maria Cinto de Biaggi, 80',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1a74928e-6d1c-40ac-a77a-e027392ba910', NOW(), NOW(), 'Responsável Comercial', 'Pure Pilates Santa Rosália',
        '5515998104400', 'ed73c9e1-e24a-4da8-b63b-3cb2a0965b40', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '39204eb2-8e0b-4fd5-9178-082cde089057', NOW(), NOW(), 'Pure Pilates Santa Rosália — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        'ed73c9e1-e24a-4da8-b63b-3cb2a0965b40', '1a74928e-6d1c-40ac-a77a-e027392ba910', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '515f4b29-9672-4658-b0e3-7d3ecbc39cd9', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Maria Cinto de Biaggi, 80)\n**Categoria:** Pilates\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515998104400',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '515f4b29-9672-4658-b0e3-7d3ecbc39cd9', 'ed73c9e1-e24a-4da8-b63b-3cb2a0965b40', '1a74928e-6d1c-40ac-a77a-e027392ba910', '39204eb2-8e0b-4fd5-9178-082cde089057',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f2054a41-afd0-442f-b7a1-2a9dd49300af', NOW(), NOW(), 'Studio Corpo & Mente Pilates', 'R. Mascarenhas Camelo, 450',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a9456f1d-2550-426f-8d72-a10201bd7cba', NOW(), NOW(), 'Responsável Comercial', 'Studio Corpo & Mente Pilates',
        '5515991442100', 'f2054a41-afd0-442f-b7a1-2a9dd49300af', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '34923b71-fe1b-4089-8971-1cbcd129957c', NOW(), NOW(), 'Studio Corpo & Mente Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        'f2054a41-afd0-442f-b7a1-2a9dd49300af', 'a9456f1d-2550-426f-8d72-a10201bd7cba', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'df5ae903-3efa-47da-badc-5b5f6bfc5be7', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 450)\n**Categoria:** Pilates\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515991442100',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'df5ae903-3efa-47da-badc-5b5f6bfc5be7', 'f2054a41-afd0-442f-b7a1-2a9dd49300af', 'a9456f1d-2550-426f-8d72-a10201bd7cba', '34923b71-fe1b-4089-8971-1cbcd129957c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '08e0ab0e-9c89-4646-9ea7-eaaf6db72085', NOW(), NOW(), 'Espaço Movimento Pilates Clássico', 'Av. Pereira da Silva, 780',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '62456c64-8a80-4883-b72a-a13f5c105ded', NOW(), NOW(), 'Responsável Comercial', 'Espaço Movimento Pilates Clássico',
        '5515981223300', '08e0ab0e-9c89-4646-9ea7-eaaf6db72085', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ce0d43aa-3272-4c98-9f4b-a4ecc0359704', NOW(), NOW(), 'Espaço Movimento Pilates Clássico — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '08e0ab0e-9c89-4646-9ea7-eaaf6db72085', '62456c64-8a80-4883-b72a-a13f5c105ded', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '23d3f16a-270a-4a6d-854d-2fd584ab8629', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 780)\n**Categoria:** Pilates\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515981223300',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '23d3f16a-270a-4a6d-854d-2fd584ab8629', '08e0ab0e-9c89-4646-9ea7-eaaf6db72085', '62456c64-8a80-4883-b72a-a13f5c105ded', 'ce0d43aa-3272-4c98-9f4b-a4ecc0359704',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e391a50a-c0ab-43d8-8e07-baa494a1148d', NOW(), NOW(), 'Studio Vital Pilates & Yoga', 'R. João dos Santos, 320',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c1342f09-de13-46cf-a0c8-0031918401e2', NOW(), NOW(), 'Responsável Comercial', 'Studio Vital Pilates & Yoga',
        '5515996551200', 'e391a50a-c0ab-43d8-8e07-baa494a1148d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7e7feaa2-9b55-4e28-ae95-fae41d900cec', NOW(), NOW(), 'Studio Vital Pilates & Yoga — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        'e391a50a-c0ab-43d8-8e07-baa494a1148d', 'c1342f09-de13-46cf-a0c8-0031918401e2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5415151d-f9bf-44cf-8d50-d23389c956f7', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. João dos Santos, 320)\n**Categoria:** Pilates & Yoga\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515996551200',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '5415151d-f9bf-44cf-8d50-d23389c956f7', 'e391a50a-c0ab-43d8-8e07-baa494a1148d', 'c1342f09-de13-46cf-a0c8-0031918401e2', '7e7feaa2-9b55-4e28-ae95-fae41d900cec',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f628db40-bacc-4fa4-bb42-baa6a39d454f', NOW(), NOW(), 'Instituto Postura & Movimento', 'Av. Pereira da Silva, 1420',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '653d962b-e59a-409e-8aab-5cd4e0718233', NOW(), NOW(), 'Responsável Comercial', 'Instituto Postura & Movimento',
        '5515997334411', 'f628db40-bacc-4fa4-bb42-baa6a39d454f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd638f4e0-24db-418b-9749-2e786073cff6', NOW(), NOW(), 'Instituto Postura & Movimento — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        'f628db40-bacc-4fa4-bb42-baa6a39d454f', '653d962b-e59a-409e-8aab-5cd4e0718233', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e7ca48e5-bee9-41c6-b817-45646faee97f', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1420)\n**Categoria:** Pilates Clínico\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515997334411',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e7ca48e5-bee9-41c6-b817-45646faee97f', 'f628db40-bacc-4fa4-bb42-baa6a39d454f', '653d962b-e59a-409e-8aab-5cd4e0718233', 'd638f4e0-24db-418b-9749-2e786073cff6',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '245bee3e-e037-4f38-8727-b651fea1a54a', NOW(), NOW(), 'Studio Funcional Rosália Fitness', 'R. Mascarenhas Camelo, 580',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a3fa8db0-b63b-4984-ad1a-f15ab1b44741', NOW(), NOW(), 'Responsável Comercial', 'Studio Funcional Rosália Fitness',
        '5515991887722', '245bee3e-e037-4f38-8727-b651fea1a54a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '86c455e4-ca6f-45ff-8e3b-c862f214d2e1', NOW(), NOW(), 'Studio Funcional Rosália Fitness — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '245bee3e-e037-4f38-8727-b651fea1a54a', 'a3fa8db0-b63b-4984-ad1a-f15ab1b44741', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ab6a3c28-2078-48a7-843f-5a8fdb2b5e2e', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 580)\n**Categoria:** Treino Funcional\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515991887722',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ab6a3c28-2078-48a7-843f-5a8fdb2b5e2e', '245bee3e-e037-4f38-8727-b651fea1a54a', 'a3fa8db0-b63b-4984-ad1a-f15ab1b44741', '86c455e4-ca6f-45ff-8e3b-c862f214d2e1',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '76dd0d6f-07f8-4ac4-b52b-3fe428b3e0e0', NOW(), NOW(), 'Personal Studio Santa Rosália', 'R. Nicolau Alonso Filho, 310',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c43bae15-9043-4046-988e-c8565d682e50', NOW(), NOW(), 'Responsável Comercial', 'Personal Studio Santa Rosália',
        '5515997116633', '76dd0d6f-07f8-4ac4-b52b-3fe428b3e0e0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3b25bec5-7c4f-4f7f-9f25-8bf1b4753d85', NOW(), NOW(), 'Personal Studio Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '76dd0d6f-07f8-4ac4-b52b-3fe428b3e0e0', 'c43bae15-9043-4046-988e-c8565d682e50', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8ec527e7-d703-4af8-b00e-fdc50cecc84b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Nicolau Alonso Filho, 310)\n**Categoria:** Personal Trainer\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997116633',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '8ec527e7-d703-4af8-b00e-fdc50cecc84b', '76dd0d6f-07f8-4ac4-b52b-3fe428b3e0e0', 'c43bae15-9043-4046-988e-c8565d682e50', '3b25bec5-7c4f-4f7f-9f25-8bf1b4753d85',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '264abc9e-2730-426a-a50e-bc5498c1c070', NOW(), NOW(), 'Espaço Zen Terapias & Pilates', 'R. Ramos de Azevedo, 140',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '95bf420c-250a-4308-8e00-9d8ae59b085f', NOW(), NOW(), 'Responsável Comercial', 'Espaço Zen Terapias & Pilates',
        '5515981559944', '264abc9e-2730-426a-a50e-bc5498c1c070', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '178e4db9-1fa4-41db-ab60-53a4dba58265', NOW(), NOW(), 'Espaço Zen Terapias & Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '264abc9e-2730-426a-a50e-bc5498c1c070', '95bf420c-250a-4308-8e00-9d8ae59b085f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ce606f8d-bcbb-48fd-b78c-050d70ee3278', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Ramos de Azevedo, 140)\n**Categoria:** Pilates & Terapias\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515981559944',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ce606f8d-bcbb-48fd-b78c-050d70ee3278', '264abc9e-2730-426a-a50e-bc5498c1c070', '95bf420c-250a-4308-8e00-9d8ae59b085f', '178e4db9-1fa4-41db-ab60-53a4dba58265',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '40fe64ae-afbc-4530-a42d-bc3f66d63077', NOW(), NOW(), 'Dra. Cauane Guelfi Estética Avançada', 'R. Rev. Henrique de Oliveira Camargo, 120',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'fad15f12-c708-4307-a602-cdc4cd48b058', NOW(), NOW(), 'Responsável Comercial', 'Dra. Cauane Guelfi Estética Avançada',
        '5515996411220', '40fe64ae-afbc-4530-a42d-bc3f66d63077', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd6dcf09f-3d4a-454c-965e-6e427db321af', NOW(), NOW(), 'Dra. Cauane Guelfi Estética Avançada — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '40fe64ae-afbc-4530-a42d-bc3f66d63077', 'fad15f12-c708-4307-a602-cdc4cd48b058', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '71c53c56-f8ec-4251-8194-8441c76eefd0', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Rev. Henrique de Oliveira Camargo, 120)\n**Categoria:** Estética Avançada\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515996411220',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '71c53c56-f8ec-4251-8194-8441c76eefd0', '40fe64ae-afbc-4530-a42d-bc3f66d63077', 'fad15f12-c708-4307-a602-cdc4cd48b058', 'd6dcf09f-3d4a-454c-965e-6e427db321af',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4f946b88-0a27-4646-8ee8-6fe20938bcd7', NOW(), NOW(), 'Rô Ferreira Estética', 'Av. Pereira da Silva, 1953, Sl 4',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6eeb657e-d74a-4832-81c4-e442e83e4062', NOW(), NOW(), 'Responsável Comercial', 'Rô Ferreira Estética',
        '5515991166474', '4f946b88-0a27-4646-8ee8-6fe20938bcd7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '27ce9ae3-e693-4f61-b0b4-4395d466da57', NOW(), NOW(), 'Rô Ferreira Estética — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '4f946b88-0a27-4646-8ee8-6fe20938bcd7', '6eeb657e-d74a-4832-81c4-e442e83e4062', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5bc661c8-7b79-466a-a9a0-93a465352a2c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1953, Sl 4)\n**Categoria:** Estética Facial\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515991166474',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '5bc661c8-7b79-466a-a9a0-93a465352a2c', '4f946b88-0a27-4646-8ee8-6fe20938bcd7', '6eeb657e-d74a-4832-81c4-e442e83e4062', '27ce9ae3-e693-4f61-b0b4-4395d466da57',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b84e38cd-c1bb-4d3a-8565-29d849d4cc86', NOW(), NOW(), 'Studio D''Elas Salão & Estética', 'Av. Pereira da Silva, 610',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ad0b7568-3286-4261-9abb-5e96eff0a7a0', NOW(), NOW(), 'Responsável Comercial', 'Studio D''Elas Salão & Estética',
        '551532338900', 'b84e38cd-c1bb-4d3a-8565-29d849d4cc86', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2717a9d4-c1ec-4407-9926-4b2d63240212', NOW(), NOW(), 'Studio D''Elas Salão & Estética — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'b84e38cd-c1bb-4d3a-8565-29d849d4cc86', 'ad0b7568-3286-4261-9abb-5e96eff0a7a0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '68e1840f-ff45-48d3-9388-975eb4e7793a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 610)\n**Categoria:** Salão & Estética\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532338900',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '68e1840f-ff45-48d3-9388-975eb4e7793a', 'b84e38cd-c1bb-4d3a-8565-29d849d4cc86', 'ad0b7568-3286-4261-9abb-5e96eff0a7a0', '2717a9d4-c1ec-4407-9926-4b2d63240212',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5ca04671-3a01-4b6f-ae69-ef62b9888a18', NOW(), NOW(), 'Espaço Bella Donna Santa Rosália', 'R. Mascarenhas Camelo, 270',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4102d2a8-3ab2-4430-961f-114d98ab2235', NOW(), NOW(), 'Responsável Comercial', 'Espaço Bella Donna Santa Rosália',
        '5515997443322', '5ca04671-3a01-4b6f-ae69-ef62b9888a18', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '02235fce-8b52-4ce5-9db8-cdcf8720dedb', NOW(), NOW(), 'Espaço Bella Donna Santa Rosália — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '5ca04671-3a01-4b6f-ae69-ef62b9888a18', '4102d2a8-3ab2-4430-961f-114d98ab2235', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9ecefaac-1866-4528-b3fd-b379e2f048ab', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 270)\n**Categoria:** Estética Corporal\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515997443322',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9ecefaac-1866-4528-b3fd-b379e2f048ab', '5ca04671-3a01-4b6f-ae69-ef62b9888a18', '4102d2a8-3ab2-4430-961f-114d98ab2235', '02235fce-8b52-4ce5-9db8-cdcf8720dedb',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '49d13d3b-ac71-433b-b112-47e42ad90218', NOW(), NOW(), 'Laser Care Depilação & Estética', 'Av. Pereira da Silva, 1250',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '58872cd1-3737-4e79-ae3e-e1b0fb485dc8', NOW(), NOW(), 'Responsável Comercial', 'Laser Care Depilação & Estética',
        '551530334410', '49d13d3b-ac71-433b-b112-47e42ad90218', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '08e45ad0-da18-42eb-8f84-e1e55e20f3c1', NOW(), NOW(), 'Laser Care Depilação & Estética — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '49d13d3b-ac71-433b-b112-47e42ad90218', '58872cd1-3737-4e79-ae3e-e1b0fb485dc8', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'febe6791-85d5-431d-9deb-87534decdf87', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1250)\n**Categoria:** Estética a Laser\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551530334410',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'febe6791-85d5-431d-9deb-87534decdf87', '49d13d3b-ac71-433b-b112-47e42ad90218', '58872cd1-3737-4e79-ae3e-e1b0fb485dc8', '08e45ad0-da18-42eb-8f84-e1e55e20f3c1',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '051bee56-811f-4da1-924a-b72311f978c3', NOW(), NOW(), 'Barbearia Tradicional Santa Rosália', 'Av. Pereira da Silva, 810',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4cd0a17d-8f2d-4e25-a413-d42ac5ed7c99', NOW(), NOW(), 'Responsável Comercial', 'Barbearia Tradicional Santa Rosália',
        '5515991228899', '051bee56-811f-4da1-924a-b72311f978c3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bbe39f35-da9f-4502-96f5-871af6f74b4c', NOW(), NOW(), 'Barbearia Tradicional Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '051bee56-811f-4da1-924a-b72311f978c3', '4cd0a17d-8f2d-4e25-a413-d42ac5ed7c99', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2f05b62a-7e27-42eb-8443-66fcf28c31fc', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 810)\n**Categoria:** Barbearia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515991228899',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '2f05b62a-7e27-42eb-8443-66fcf28c31fc', '051bee56-811f-4da1-924a-b72311f978c3', '4cd0a17d-8f2d-4e25-a413-d42ac5ed7c99', 'bbe39f35-da9f-4502-96f5-871af6f74b4c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'db9f32c1-613b-4e6b-bd45-2c06a37104d5', NOW(), NOW(), 'Ateliê da Beleza & Sobrancelhas', 'R. Nicolau Alonso Filho, 115',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6e9a2837-3c08-4fea-a676-8c6c37b4b338', NOW(), NOW(), 'Responsável Comercial', 'Ateliê da Beleza & Sobrancelhas',
        '5515998337711', 'db9f32c1-613b-4e6b-bd45-2c06a37104d5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4cc29341-3e79-4737-b676-47f45b17d0c8', NOW(), NOW(), 'Ateliê da Beleza & Sobrancelhas — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'db9f32c1-613b-4e6b-bd45-2c06a37104d5', '6e9a2837-3c08-4fea-a676-8c6c37b4b338', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e1d7ac76-16c6-4f6c-a525-bf24091a7faa', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Nicolau Alonso Filho, 115)\n**Categoria:** Micropigmentação\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515998337711',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e1d7ac76-16c6-4f6c-a525-bf24091a7faa', 'db9f32c1-613b-4e6b-bd45-2c06a37104d5', '6e9a2837-3c08-4fea-a676-8c6c37b4b338', '4cc29341-3e79-4737-b676-47f45b17d0c8',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '97c72aff-0ceb-4fdd-a33c-5d1711025af2', NOW(), NOW(), 'Clínica de Estética Silhouette', 'Av. Pereira da Silva, 1540',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6a5f9913-b5e0-46a8-bfdd-577a77d5ac7c', NOW(), NOW(), 'Responsável Comercial', 'Clínica de Estética Silhouette',
        '5515996225544', '97c72aff-0ceb-4fdd-a33c-5d1711025af2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '99b9908b-f6d2-42ee-8b30-18fcd45a445c', NOW(), NOW(), 'Clínica de Estética Silhouette — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '97c72aff-0ceb-4fdd-a33c-5d1711025af2', '6a5f9913-b5e0-46a8-bfdd-577a77d5ac7c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '31c35cda-6d8b-420d-a1f3-5b83381ac25a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1540)\n**Categoria:** Estética Avançada\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515996225544',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '31c35cda-6d8b-420d-a1f3-5b83381ac25a', '97c72aff-0ceb-4fdd-a33c-5d1711025af2', '6a5f9913-b5e0-46a8-bfdd-577a77d5ac7c', '99b9908b-f6d2-42ee-8b30-18fcd45a445c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ae4f91d3-ffcf-4bf6-aa91-5b1f5c5233a5', NOW(), NOW(), 'Espaço Homem Barbearia & Estética', 'R. Maria Cinto de Biaggi, 190',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b7577a1a-1ee8-4038-bd3e-9c70f5748193', NOW(), NOW(), 'Responsável Comercial', 'Espaço Homem Barbearia & Estética',
        '551532114400', 'ae4f91d3-ffcf-4bf6-aa91-5b1f5c5233a5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a489241c-dbb2-4cc9-915b-d28df2042184', NOW(), NOW(), 'Espaço Homem Barbearia & Estética — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'ae4f91d3-ffcf-4bf6-aa91-5b1f5c5233a5', 'b7577a1a-1ee8-4038-bd3e-9c70f5748193', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '67a0fc44-a43b-4771-8cbe-e4fd2b451c74', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Maria Cinto de Biaggi, 190)\n**Categoria:** Barbearia Masculina\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532114400',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '67a0fc44-a43b-4771-8cbe-e4fd2b451c74', 'ae4f91d3-ffcf-4bf6-aa91-5b1f5c5233a5', 'b7577a1a-1ee8-4038-bd3e-9c70f5748193', 'a489241c-dbb2-4cc9-915b-d28df2042184',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b0d2d171-39ab-492d-8de6-ef2a8cad63bd', NOW(), NOW(), 'Studio Nails & Beauty Santa Rosália', 'R. Mascarenhas Camelo, 125',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f9187cad-56f5-42e7-b098-43546978c1e2', NOW(), NOW(), 'Responsável Comercial', 'Studio Nails & Beauty Santa Rosália',
        '5515997661188', 'b0d2d171-39ab-492d-8de6-ef2a8cad63bd', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b993068a-5708-41f4-880c-4dc8eb5742d9', NOW(), NOW(), 'Studio Nails & Beauty Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'b0d2d171-39ab-492d-8de6-ef2a8cad63bd', 'f9187cad-56f5-42e7-b098-43546978c1e2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '108c1e11-08bc-416c-a6f4-f7e6fd1ccf97', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 125)\n**Categoria:** Unhas & Beleza\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997661188',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '108c1e11-08bc-416c-a6f4-f7e6fd1ccf97', 'b0d2d171-39ab-492d-8de6-ef2a8cad63bd', 'f9187cad-56f5-42e7-b098-43546978c1e2', 'b993068a-5708-41f4-880c-4dc8eb5742d9',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4ec96dc7-a85b-49c4-8cf3-dd36edb46cc7', NOW(), NOW(), 'Vet Care Saúde Animal', 'Av. Pereira da Silva, 68',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e6475b68-0500-41b0-b5aa-669760240f5f', NOW(), NOW(), 'Responsável Comercial', 'Vet Care Saúde Animal',
        '5515981722170', '4ec96dc7-a85b-49c4-8cf3-dd36edb46cc7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '219d9a78-7892-41de-aba7-3ba998e85186', NOW(), NOW(), 'Vet Care Saúde Animal — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '4ec96dc7-a85b-49c4-8cf3-dd36edb46cc7', 'e6475b68-0500-41b0-b5aa-669760240f5f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '53e21a87-3256-49af-b97f-f3363dc5887f', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 68)\n**Categoria:** Clínica Veterinária\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515981722170',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '53e21a87-3256-49af-b97f-f3363dc5887f', '4ec96dc7-a85b-49c4-8cf3-dd36edb46cc7', 'e6475b68-0500-41b0-b5aa-669760240f5f', '219d9a78-7892-41de-aba7-3ba998e85186',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0560e69f-524d-462a-be84-1ba2ac9d197b', NOW(), NOW(), 'Deniane Almeida Fisiovet', 'Av. Pereira da Silva, 68',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '45540f8f-31b3-452d-af35-ae9c9f9b890c', NOW(), NOW(), 'Responsável Comercial', 'Deniane Almeida Fisiovet',
        '5515996841434', '0560e69f-524d-462a-be84-1ba2ac9d197b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '01d8b35e-e3f4-4f97-881e-f366f18b36e6', NOW(), NOW(), 'Deniane Almeida Fisiovet — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '0560e69f-524d-462a-be84-1ba2ac9d197b', '45540f8f-31b3-452d-af35-ae9c9f9b890c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1e8f6bbb-9b63-4e16-a0fd-a016257db01c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 68)\n**Categoria:** Reabilitação Veterinária\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515996841434',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1e8f6bbb-9b63-4e16-a0fd-a016257db01c', '0560e69f-524d-462a-be84-1ba2ac9d197b', '45540f8f-31b3-452d-af35-ae9c9f9b890c', '01d8b35e-e3f4-4f97-881e-f366f18b36e6',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9e98ee54-8c06-47ca-be8f-8ac4b2597cf9', NOW(), NOW(), 'BastVet Centro Veterinário', 'R. José Del Ben, 140',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a2f6a624-38a0-469b-ac37-cbfa5b27db93', NOW(), NOW(), 'Responsável Comercial', 'BastVet Centro Veterinário',
        '551532328811', '9e98ee54-8c06-47ca-be8f-8ac4b2597cf9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e2e7b9be-2777-40b5-a71b-23fa81cd5120', NOW(), NOW(), 'BastVet Centro Veterinário — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '9e98ee54-8c06-47ca-be8f-8ac4b2597cf9', 'a2f6a624-38a0-469b-ac37-cbfa5b27db93', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ba042b95-9848-4dac-a3bf-2f85d0e6bc2c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. José Del Ben, 140)\n**Categoria:** Hospital Veterinário\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532328811',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ba042b95-9848-4dac-a3bf-2f85d0e6bc2c', '9e98ee54-8c06-47ca-be8f-8ac4b2597cf9', 'a2f6a624-38a0-469b-ac37-cbfa5b27db93', 'e2e7b9be-2777-40b5-a71b-23fa81cd5120',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9fb1587a-36e3-4d8b-aa59-d078fcc977e4', NOW(), NOW(), 'Pet Shop & Clínica Santa Rosália', 'Av. Pereira da Silva, 940',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7be15fd8-d8bb-49a6-baab-2bda002c8fbf', NOW(), NOW(), 'Responsável Comercial', 'Pet Shop & Clínica Santa Rosália',
        '551532345566', '9fb1587a-36e3-4d8b-aa59-d078fcc977e4', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a0eb4467-0600-4a8c-9317-9a2511b4d84a', NOW(), NOW(), 'Pet Shop & Clínica Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '9fb1587a-36e3-4d8b-aa59-d078fcc977e4', '7be15fd8-d8bb-49a6-baab-2bda002c8fbf', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '10e02a79-611c-4944-9529-2d0a8be81926', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 940)\n**Categoria:** Pet Shop & Banho\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532345566',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '10e02a79-611c-4944-9529-2d0a8be81926', '9fb1587a-36e3-4d8b-aa59-d078fcc977e4', '7be15fd8-d8bb-49a6-baab-2bda002c8fbf', 'a0eb4467-0600-4a8c-9317-9a2511b4d84a',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '941cfeb6-65e3-43c3-82b3-1d80904ad904', NOW(), NOW(), 'Boutique Animal Estética Pet', 'R. Nicolau Alonso Filho, 420',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '09656453-686a-40eb-81f7-eab51fc08ec2', NOW(), NOW(), 'Responsável Comercial', 'Boutique Animal Estética Pet',
        '5515991332211', '941cfeb6-65e3-43c3-82b3-1d80904ad904', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '04178882-2083-47b4-a82d-31926369dd35', NOW(), NOW(), 'Boutique Animal Estética Pet — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '941cfeb6-65e3-43c3-82b3-1d80904ad904', '09656453-686a-40eb-81f7-eab51fc08ec2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f7fd4b55-34f7-419c-b9b4-461f85f8b499', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Nicolau Alonso Filho, 420)\n**Categoria:** Estética Pet\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515991332211',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'f7fd4b55-34f7-419c-b9b4-461f85f8b499', '941cfeb6-65e3-43c3-82b3-1d80904ad904', '09656453-686a-40eb-81f7-eab51fc08ec2', '04178882-2083-47b4-a82d-31926369dd35',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2e650e38-4eb9-4257-8dab-3595ccd3574e', NOW(), NOW(), 'Consultório Veterinário Dr. Marcelo', 'R. Mascarenhas Camelo, 380',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd056f207-ab8c-421c-bce2-69ccd1cc254c', NOW(), NOW(), 'Responsável Comercial', 'Consultório Veterinário Dr. Marcelo',
        '551532317788', '2e650e38-4eb9-4257-8dab-3595ccd3574e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c7856026-d051-4bfe-aad6-f5a37a94527d', NOW(), NOW(), 'Consultório Veterinário Dr. Marcelo — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '2e650e38-4eb9-4257-8dab-3595ccd3574e', 'd056f207-ab8c-421c-bce2-69ccd1cc254c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '785bd6ec-97aa-4699-a39e-e5b2c19457b6', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 380)\n**Categoria:** Veterinária\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532317788',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '785bd6ec-97aa-4699-a39e-e5b2c19457b6', '2e650e38-4eb9-4257-8dab-3595ccd3574e', 'd056f207-ab8c-421c-bce2-69ccd1cc254c', 'c7856026-d051-4bfe-aad6-f5a37a94527d',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd2ec16c2-f36b-4e8c-b8d1-37a5c57163f1', NOW(), NOW(), 'Amigo dos Bichos Pet Shop', 'Av. Pereira da Silva, 1340',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '28f5d70f-200e-4657-929f-6eda8683dbe3', NOW(), NOW(), 'Responsável Comercial', 'Amigo dos Bichos Pet Shop',
        '5515997448822', 'd2ec16c2-f36b-4e8c-b8d1-37a5c57163f1', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2b965f28-0adf-4f6f-b46c-6b838ec72f41', NOW(), NOW(), 'Amigo dos Bichos Pet Shop — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'd2ec16c2-f36b-4e8c-b8d1-37a5c57163f1', '28f5d70f-200e-4657-929f-6eda8683dbe3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cc19c972-ad7f-44f0-8478-dff9211a8b44', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1340)\n**Categoria:** Pet Shop\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997448822',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'cc19c972-ad7f-44f0-8478-dff9211a8b44', 'd2ec16c2-f36b-4e8c-b8d1-37a5c57163f1', '28f5d70f-200e-4657-929f-6eda8683dbe3', '2b965f28-0adf-4f6f-b46c-6b838ec72f41',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1394a77e-57f3-420d-87c2-491a4ec81fe4', NOW(), NOW(), 'Espaço Pet Spa & Hotelzinho', 'R. Ramos de Azevedo, 210',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5e980220-3015-4bee-ae63-ec29dd0bd8f1', NOW(), NOW(), 'Responsável Comercial', 'Espaço Pet Spa & Hotelzinho',
        '5515981446655', '1394a77e-57f3-420d-87c2-491a4ec81fe4', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e3be23bc-cdf1-4c9d-95c0-a6effa68148b', NOW(), NOW(), 'Espaço Pet Spa & Hotelzinho — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '1394a77e-57f3-420d-87c2-491a4ec81fe4', '5e980220-3015-4bee-ae63-ec29dd0bd8f1', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1cb97c97-1e82-4ee6-af92-d19c0fd11efb', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Ramos de Azevedo, 210)\n**Categoria:** Hotel Pet\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515981446655',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1cb97c97-1e82-4ee6-af92-d19c0fd11efb', '1394a77e-57f3-420d-87c2-491a4ec81fe4', '5e980220-3015-4bee-ae63-ec29dd0bd8f1', 'e3be23bc-cdf1-4c9d-95c0-a6effa68148b',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2810f703-6ce4-452d-b40c-7ed6b889f26e', NOW(), NOW(), 'Izakaya Tsuchi Gastronomia Japonesa', 'Av. Pereira da Silva, 1867',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3166692f-60e1-418b-bd29-a57aabd7851d', NOW(), NOW(), 'Responsável Comercial', 'Izakaya Tsuchi Gastronomia Japonesa',
        '551532114258', '2810f703-6ce4-452d-b40c-7ed6b889f26e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '88347693-3822-4640-a2b3-18587621bdd9', NOW(), NOW(), 'Izakaya Tsuchi Gastronomia Japonesa — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '2810f703-6ce4-452d-b40c-7ed6b889f26e', '3166692f-60e1-418b-bd29-a57aabd7851d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e5437f06-2cf7-4fea-bd1e-db9b4e68d97c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1867)\n**Categoria:** Gastronomia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532114258',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e5437f06-2cf7-4fea-bd1e-db9b4e68d97c', '2810f703-6ce4-452d-b40c-7ed6b889f26e', '3166692f-60e1-418b-bd29-a57aabd7851d', '88347693-3822-4640-a2b3-18587621bdd9',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9cbeccd3-ded7-4240-8eb7-1c21d44f2fc5', NOW(), NOW(), 'Café com Gato Sorocaba', 'Av. Pereira da Silva, 866',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f2eb2f54-2ffd-491b-bfec-952878fff354', NOW(), NOW(), 'Responsável Comercial', 'Café com Gato Sorocaba',
        '551533260658', '9cbeccd3-ded7-4240-8eb7-1c21d44f2fc5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '77aa301a-22b6-4b39-8bef-7e2db257a38f', NOW(), NOW(), 'Café com Gato Sorocaba — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '9cbeccd3-ded7-4240-8eb7-1c21d44f2fc5', 'f2eb2f54-2ffd-491b-bfec-952878fff354', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd0bcc282-7909-4847-8571-2f11a895bb67', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 866)\n**Categoria:** Cafeteria Conceito\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551533260658',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'd0bcc282-7909-4847-8571-2f11a895bb67', '9cbeccd3-ded7-4240-8eb7-1c21d44f2fc5', 'f2eb2f54-2ffd-491b-bfec-952878fff354', '77aa301a-22b6-4b39-8bef-7e2db257a38f',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0ea21144-799e-4dec-b239-24caf1e93c92', NOW(), NOW(), 'Di Garden Restaurante & Eventos', 'Av. Pereira da Silva, 272',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'def9c3a9-9367-48b7-b961-d690689ff06d', NOW(), NOW(), 'Responsável Comercial', 'Di Garden Restaurante & Eventos',
        '551532323152', '0ea21144-799e-4dec-b239-24caf1e93c92', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ed896c4d-f4e9-48ae-b98d-038682ce2d88', NOW(), NOW(), 'Di Garden Restaurante & Eventos — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '0ea21144-799e-4dec-b239-24caf1e93c92', 'def9c3a9-9367-48b7-b961-d690689ff06d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '47506c6f-f399-49e7-a647-ab498dc09986', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 272)\n**Categoria:** Restaurante\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532323152',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '47506c6f-f399-49e7-a647-ab498dc09986', '0ea21144-799e-4dec-b239-24caf1e93c92', 'def9c3a9-9367-48b7-b961-d690689ff06d', 'ed896c4d-f4e9-48ae-b98d-038682ce2d88',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '35eb4ee3-2a81-4203-8a5d-6fbe1064090b', NOW(), NOW(), 'Cão Véio Sorocaba Gastropub', 'Av. Pereira da Silva, 1919',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4418452c-36c6-4dde-abdc-f549d2e3af27', NOW(), NOW(), 'Responsável Comercial', 'Cão Véio Sorocaba Gastropub',
        '551530335500', '35eb4ee3-2a81-4203-8a5d-6fbe1064090b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cb4b865b-b061-4687-afa0-c5e5e4e2c636', NOW(), NOW(), 'Cão Véio Sorocaba Gastropub — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '35eb4ee3-2a81-4203-8a5d-6fbe1064090b', '4418452c-36c6-4dde-abdc-f549d2e3af27', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b11d7915-4ac2-4213-a41c-91b83b82a0e7', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1919)\n**Categoria:** Gastropub\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551530335500',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'b11d7915-4ac2-4213-a41c-91b83b82a0e7', '35eb4ee3-2a81-4203-8a5d-6fbe1064090b', '4418452c-36c6-4dde-abdc-f549d2e3af27', 'cb4b865b-b061-4687-afa0-c5e5e4e2c636',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '83db935b-b44d-4164-81ad-cf84d7b46439', NOW(), NOW(), 'Bistrô da Praça Santa Rosália', 'Praça Pio XII, 45',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '60d6dd64-513b-4847-9f39-18601af37bc4', NOW(), NOW(), 'Responsável Comercial', 'Bistrô da Praça Santa Rosália',
        '551532349911', '83db935b-b44d-4164-81ad-cf84d7b46439', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '34488f15-8dc2-42e0-adb6-c20765d187cc', NOW(), NOW(), 'Bistrô da Praça Santa Rosália — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '83db935b-b44d-4164-81ad-cf84d7b46439', '60d6dd64-513b-4847-9f39-18601af37bc4', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '13b3d120-c141-4fb3-8770-3c5b99364726', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Praça Pio XII, 45)\n**Categoria:** Bistrô\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532349911',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '13b3d120-c141-4fb3-8770-3c5b99364726', '83db935b-b44d-4164-81ad-cf84d7b46439', '60d6dd64-513b-4847-9f39-18601af37bc4', '34488f15-8dc2-42e0-adb6-c20765d187cc',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'db1266da-ba24-423c-8bd9-e65d4b98851a', NOW(), NOW(), 'Forneria & Pizzaria Santa Rosália', 'Av. Pereira da Silva, 1120',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '308ad457-a06b-4c5e-b7b8-97a9a65df732', NOW(), NOW(), 'Responsável Comercial', 'Forneria & Pizzaria Santa Rosália',
        '551532337744', 'db1266da-ba24-423c-8bd9-e65d4b98851a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2845026a-1c87-414d-b0a6-ca32d16c4808', NOW(), NOW(), 'Forneria & Pizzaria Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'db1266da-ba24-423c-8bd9-e65d4b98851a', '308ad457-a06b-4c5e-b7b8-97a9a65df732', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '764f8189-081b-44ef-b78a-5d841de2e37f', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1120)\n**Categoria:** Pizzaria Artesanal\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532337744',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '764f8189-081b-44ef-b78a-5d841de2e37f', 'db1266da-ba24-423c-8bd9-e65d4b98851a', '308ad457-a06b-4c5e-b7b8-97a9a65df732', '2845026a-1c87-414d-b0a6-ca32d16c4808',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '50f3104c-c334-4a94-a4b9-c8c4c1040e15', NOW(), NOW(), 'Empório Gourmet Santa Rosália', 'Av. Pereira da Silva, 640',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'aed29d26-9e68-45b1-bec3-6475ccc200d7', NOW(), NOW(), 'Responsável Comercial', 'Empório Gourmet Santa Rosália',
        '5515998221144', '50f3104c-c334-4a94-a4b9-c8c4c1040e15', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '643c69e4-3d8e-4524-b4ee-8f6b16c4d6ef', NOW(), NOW(), 'Empório Gourmet Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '50f3104c-c334-4a94-a4b9-c8c4c1040e15', 'aed29d26-9e68-45b1-bec3-6475ccc200d7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1713c432-a940-409a-8280-400d4876068b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 640)\n**Categoria:** Empório & Vinhos\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515998221144',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1713c432-a940-409a-8280-400d4876068b', '50f3104c-c334-4a94-a4b9-c8c4c1040e15', 'aed29d26-9e68-45b1-bec3-6475ccc200d7', '643c69e4-3d8e-4524-b4ee-8f6b16c4d6ef',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '532e09e3-c33f-46cb-a225-7262daac61e3', NOW(), NOW(), 'Doce Encanto Confeitaria Fina', 'R. Mascarenhas Camelo, 150',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8f06c150-8e3d-4790-9dca-bab6d9b42f5e', NOW(), NOW(), 'Responsável Comercial', 'Doce Encanto Confeitaria Fina',
        '5515991554433', '532e09e3-c33f-46cb-a225-7262daac61e3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c8b00373-bb39-437f-b435-ff191b9e0d0c', NOW(), NOW(), 'Doce Encanto Confeitaria Fina — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '532e09e3-c33f-46cb-a225-7262daac61e3', '8f06c150-8e3d-4790-9dca-bab6d9b42f5e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '610a3f6e-3941-44fb-afd6-81cba4b911b1', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 150)\n**Categoria:** Confeitaria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515991554433',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '610a3f6e-3941-44fb-afd6-81cba4b911b1', '532e09e3-c33f-46cb-a225-7262daac61e3', '8f06c150-8e3d-4790-9dca-bab6d9b42f5e', 'c8b00373-bb39-437f-b435-ff191b9e0d0c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5fd8eee8-9fb5-4d74-97dd-4a30e2f61512', NOW(), NOW(), 'Choperia & Espetaria Santa Rosália', 'Av. Pereira da Silva, 1720',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bbf734f8-1053-4139-b2e8-92cf5e269677', NOW(), NOW(), 'Responsável Comercial', 'Choperia & Espetaria Santa Rosália',
        '5515997339900', '5fd8eee8-9fb5-4d74-97dd-4a30e2f61512', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd38de9c2-8d00-42c1-b60c-bf10624fe616', NOW(), NOW(), 'Choperia & Espetaria Santa Rosália — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '5fd8eee8-9fb5-4d74-97dd-4a30e2f61512', 'bbf734f8-1053-4139-b2e8-92cf5e269677', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f5bec6e3-270c-45e1-bcc0-ba58e9c71953', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1720)\n**Categoria:** Bar & Gastronomia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515997339900',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'f5bec6e3-270c-45e1-bcc0-ba58e9c71953', '5fd8eee8-9fb5-4d74-97dd-4a30e2f61512', 'bbf734f8-1053-4139-b2e8-92cf5e269677', 'd38de9c2-8d00-42c1-b60c-bf10624fe616',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6a202c86-14a4-4cdc-827f-fe5990d5fd47', NOW(), NOW(), 'Motory Locadora & Veículos', 'Av. Pereira da Silva, 1312',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9238bd76-10af-4ae6-bd67-bcacbc0e2d6a', NOW(), NOW(), 'Responsável Comercial', 'Motory Locadora & Veículos',
        '551532323002', '6a202c86-14a4-4cdc-827f-fe5990d5fd47', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6557c698-6eea-4cfd-91de-29a08def391c', NOW(), NOW(), 'Motory Locadora & Veículos — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '6a202c86-14a4-4cdc-827f-fe5990d5fd47', '9238bd76-10af-4ae6-bd67-bcacbc0e2d6a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '76216faf-a799-4df4-aa56-be198bff0572', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1312)\n**Categoria:** Locadora de Carros\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532323002',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '76216faf-a799-4df4-aa56-be198bff0572', '6a202c86-14a4-4cdc-827f-fe5990d5fd47', '9238bd76-10af-4ae6-bd67-bcacbc0e2d6a', '6557c698-6eea-4cfd-91de-29a08def391c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b05cda95-9c80-4a72-a8a4-639ecac84e53', NOW(), NOW(), 'Posto CIC Santa Rosália & Conveniência', 'Av. Pereira da Silva, 557',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd8d005cc-47e4-4a53-acd2-0276568dc751', NOW(), NOW(), 'Responsável Comercial', 'Posto CIC Santa Rosália & Conveniência',
        '551532344782', 'b05cda95-9c80-4a72-a8a4-639ecac84e53', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5bb31b54-43ad-4ad5-85c4-b4a9971a2ef9', NOW(), NOW(), 'Posto CIC Santa Rosália & Conveniência — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'b05cda95-9c80-4a72-a8a4-639ecac84e53', 'd8d005cc-47e4-4a53-acd2-0276568dc751', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '832fb844-1879-4c22-91ef-68bb7b2d4a67', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 557)\n**Categoria:** Posto & Serviços\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532344782',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '832fb844-1879-4c22-91ef-68bb7b2d4a67', 'b05cda95-9c80-4a72-a8a4-639ecac84e53', 'd8d005cc-47e4-4a53-acd2-0276568dc751', '5bb31b54-43ad-4ad5-85c4-b4a9971a2ef9',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '87b5fa95-b7c0-4875-9898-154e809cee69', NOW(), NOW(), 'Centro Automotivo Pereira da Silva', 'Av. Pereira da Silva, 480',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2f7504d5-8fce-496e-bd8d-793fd4a600a3', NOW(), NOW(), 'Responsável Comercial', 'Centro Automotivo Pereira da Silva',
        '551532336622', '87b5fa95-b7c0-4875-9898-154e809cee69', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b928f5b7-6054-4e11-a336-0a10a1ad937c', NOW(), NOW(), 'Centro Automotivo Pereira da Silva — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '87b5fa95-b7c0-4875-9898-154e809cee69', '2f7504d5-8fce-496e-bd8d-793fd4a600a3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a2e97254-8c26-44b9-b434-a627c48c4106', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 480)\n**Categoria:** Oficina Mecânica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532336622',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'a2e97254-8c26-44b9-b434-a627c48c4106', '87b5fa95-b7c0-4875-9898-154e809cee69', '2f7504d5-8fce-496e-bd8d-793fd4a600a3', 'b928f5b7-6054-4e11-a336-0a10a1ad937c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b7d229e2-1c41-476f-8094-0bf7b43481f6', NOW(), NOW(), 'Santa Rosália Pneus & Alinhamento', 'Av. Pereira da Silva, 1490',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a27383a7-8e36-4a02-b9ab-4a5a67918431', NOW(), NOW(), 'Responsável Comercial', 'Santa Rosália Pneus & Alinhamento',
        '551532318844', 'b7d229e2-1c41-476f-8094-0bf7b43481f6', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '80882a8f-bc24-4df1-82b5-8454ec5cadc7', NOW(), NOW(), 'Santa Rosália Pneus & Alinhamento — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'b7d229e2-1c41-476f-8094-0bf7b43481f6', 'a27383a7-8e36-4a02-b9ab-4a5a67918431', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '182d2ec8-1524-4fa8-b5e6-af417fd41d67', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1490)\n**Categoria:** Auto Center\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532318844',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '182d2ec8-1524-4fa8-b5e6-af417fd41d67', 'b7d229e2-1c41-476f-8094-0bf7b43481f6', 'a27383a7-8e36-4a02-b9ab-4a5a67918431', '80882a8f-bc24-4df1-82b5-8454ec5cadc7',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '64313100-14ff-458b-9c99-97fa9bbe2303', NOW(), NOW(), 'Colégio Cristão Almeida Barros', 'R. Aparecida, 780',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '91bb7045-6962-4440-86e0-577c9f73200f', NOW(), NOW(), 'Responsável Comercial', 'Colégio Cristão Almeida Barros',
        '551532326090', '64313100-14ff-458b-9c99-97fa9bbe2303', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '897b21df-9434-40bc-81a9-1aad41c54447', NOW(), NOW(), 'Colégio Cristão Almeida Barros — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '64313100-14ff-458b-9c99-97fa9bbe2303', '91bb7045-6962-4440-86e0-577c9f73200f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a2a9e78a-da2a-445e-8aca-ea0c64a7cc98', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Aparecida, 780)\n**Categoria:** Educação / Escola\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532326090',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'a2a9e78a-da2a-445e-8aca-ea0c64a7cc98', '64313100-14ff-458b-9c99-97fa9bbe2303', '91bb7045-6962-4440-86e0-577c9f73200f', '897b21df-9434-40bc-81a9-1aad41c54447',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1120b98e-babd-4810-bc52-d42f1fb9eb90', NOW(), NOW(), 'Escola de Música Notas de Ouro', 'R. Mascarenhas Camelo, 210',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '030fc378-e784-44b1-8408-2df48cff21b6', NOW(), NOW(), 'Responsável Comercial', 'Escola de Música Notas de Ouro',
        '5515996118833', '1120b98e-babd-4810-bc52-d42f1fb9eb90', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c6868c10-7286-4d2a-91e9-c58594312ef8', NOW(), NOW(), 'Escola de Música Notas de Ouro — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '1120b98e-babd-4810-bc52-d42f1fb9eb90', '030fc378-e784-44b1-8408-2df48cff21b6', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '286dd413-44f6-4cfe-b3c5-bf18e2b23cb5', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Mascarenhas Camelo, 210)\n**Categoria:** Escola de Música\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 5515996118833',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '286dd413-44f6-4cfe-b3c5-bf18e2b23cb5', '1120b98e-babd-4810-bc52-d42f1fb9eb90', '030fc378-e784-44b1-8408-2df48cff21b6', 'c6868c10-7286-4d2a-91e9-c58594312ef8',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '80eeb5db-3337-4880-bc1c-476a1389413e', NOW(), NOW(), 'Escola de Idiomas Santa Rosália', 'Av. Pereira da Silva, 1020',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1704d5dc-7b1e-4bf4-8442-4114312be413', NOW(), NOW(), 'Responsável Comercial', 'Escola de Idiomas Santa Rosália',
        '551532341122', '80eeb5db-3337-4880-bc1c-476a1389413e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6b8947f6-c719-47a2-ade5-ebfdb085c32d', NOW(), NOW(), 'Escola de Idiomas Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '80eeb5db-3337-4880-bc1c-476a1389413e', '1704d5dc-7b1e-4bf4-8442-4114312be413', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1854784b-d625-4ba4-87d2-aaddc81ca554', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (Av. Pereira da Silva, 1020)\n**Categoria:** Idiomas\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532341122',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1854784b-d625-4ba4-87d2-aaddc81ca554', '80eeb5db-3337-4880-bc1c-476a1389413e', '1704d5dc-7b1e-4bf4-8442-4114312be413', '6b8947f6-c719-47a2-ade5-ebfdb085c32d',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c5ce9d60-aa52-40f5-9db6-69af171cda9b', NOW(), NOW(), 'Lavanderia Express Santa Rosália', 'R. Maria Cinto de Biaggi, 230',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b20b3c38-3d04-4263-9a61-1f726c7d4662', NOW(), NOW(), 'Responsável Comercial', 'Lavanderia Express Santa Rosália',
        '5515997224488', 'c5ce9d60-aa52-40f5-9db6-69af171cda9b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f33be97f-c7e7-4b52-b551-bae3aff7f909', NOW(), NOW(), 'Lavanderia Express Santa Rosália — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'c5ce9d60-aa52-40f5-9db6-69af171cda9b', 'b20b3c38-3d04-4263-9a61-1f726c7d4662', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b9d15851-b14a-4c10-a58c-26552855aae8', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Santa Rosália (R. Maria Cinto de Biaggi, 230)\n**Categoria:** Lavanderia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997224488',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'b9d15851-b14a-4c10-a58c-26552855aae8', 'c5ce9d60-aa52-40f5-9db6-69af171cda9b', 'b20b3c38-3d04-4263-9a61-1f726c7d4662', 'f33be97f-c7e7-4b52-b551-bae3aff7f909',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9551843d-2c31-4222-9cf8-384499d645b0', NOW(), NOW(), 'Brasilândia Odontologia Especializada', 'Av. Brasil, 420',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a415ac44-e6f1-4a8e-ac2f-743d65ed7dde', NOW(), NOW(), 'Responsável Comercial', 'Brasilândia Odontologia Especializada',
        '551532314411', '9551843d-2c31-4222-9cf8-384499d645b0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e756d1b0-d8dd-4be5-8fbc-9649218013f1', NOW(), NOW(), 'Brasilândia Odontologia Especializada — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '9551843d-2c31-4222-9cf8-384499d645b0', 'a415ac44-e6f1-4a8e-ac2f-743d65ed7dde', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'befc74ce-1651-44dc-91d0-d4fa524205d7', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 420)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532314411',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'befc74ce-1651-44dc-91d0-d4fa524205d7', '9551843d-2c31-4222-9cf8-384499d645b0', 'a415ac44-e6f1-4a8e-ac2f-743d65ed7dde', 'e756d1b0-d8dd-4be5-8fbc-9649218013f1',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '192ff4fa-6328-4e51-9640-87e8721630b9', NOW(), NOW(), 'Clínica Dr. Marcos Dental', 'R. Maciel Vaz, 180',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5dd65e66-98b6-4178-8c30-b1351ea86596', NOW(), NOW(), 'Responsável Comercial', 'Clínica Dr. Marcos Dental',
        '5515997123344', '192ff4fa-6328-4e51-9640-87e8721630b9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd391c398-b810-46f6-8c49-d136e22278ce', NOW(), NOW(), 'Clínica Dr. Marcos Dental — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '192ff4fa-6328-4e51-9640-87e8721630b9', '5dd65e66-98b6-4178-8c30-b1351ea86596', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'edd40fbf-33b9-4670-9038-eb56a312ab18', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 180)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515997123344',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'edd40fbf-33b9-4670-9038-eb56a312ab18', '192ff4fa-6328-4e51-9640-87e8721630b9', '5dd65e66-98b6-4178-8c30-b1351ea86596', 'd391c398-b810-46f6-8c49-d136e22278ce',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c6dd1f2a-5ce7-4509-b9d8-cb45b3602bdc', NOW(), NOW(), 'Dra. Camila Odontologia e Estética', 'R. Olavo Bilac, 95',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0c3d9c2d-b4bc-4827-84e1-98ce6429352e', NOW(), NOW(), 'Responsável Comercial', 'Dra. Camila Odontologia e Estética',
        '5515991448855', 'c6dd1f2a-5ce7-4509-b9d8-cb45b3602bdc', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'fc7b16c8-c0e9-43c6-88a6-7999a9b2804a', NOW(), NOW(), 'Dra. Camila Odontologia e Estética — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'c6dd1f2a-5ce7-4509-b9d8-cb45b3602bdc', '0c3d9c2d-b4bc-4827-84e1-98ce6429352e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5c0becb4-2012-43e3-ab53-13799db4f468', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 95)\n**Categoria:** Odontologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515991448855',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '5c0becb4-2012-43e3-ab53-13799db4f468', 'c6dd1f2a-5ce7-4509-b9d8-cb45b3602bdc', '0c3d9c2d-b4bc-4827-84e1-98ce6429352e', 'fc7b16c8-c0e9-43c6-88a6-7999a9b2804a',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e0e9df6b-8fa1-4456-90ee-af922d8be46f', NOW(), NOW(), 'Fisioterapia Integrada Brasilândia', 'Av. Brasil, 780',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9c09d014-4ea3-4c59-8032-f2a6ba4a663e', NOW(), NOW(), 'Responsável Comercial', 'Fisioterapia Integrada Brasilândia',
        '551532341290', 'e0e9df6b-8fa1-4456-90ee-af922d8be46f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '39a04925-30e0-4d18-975f-b4d43a48c1f4', NOW(), NOW(), 'Fisioterapia Integrada Brasilândia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'e0e9df6b-8fa1-4456-90ee-af922d8be46f', '9c09d014-4ea3-4c59-8032-f2a6ba4a663e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5b9715b2-d228-4aa5-892f-578678417e8b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 780)\n**Categoria:** Fisioterapia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 551532341290',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '5b9715b2-d228-4aa5-892f-578678417e8b', 'e0e9df6b-8fa1-4456-90ee-af922d8be46f', '9c09d014-4ea3-4c59-8032-f2a6ba4a663e', '39a04925-30e0-4d18-975f-b4d43a48c1f4',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2f54a815-7536-4104-89fd-73d7540b855e', NOW(), NOW(), 'Consultório de Psicologia & Família', 'R. Castanho Taques, 110',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ca7b076f-7f36-4d46-95cc-81de9e52f81b', NOW(), NOW(), 'Responsável Comercial', 'Consultório de Psicologia & Família',
        '5515981336622', '2f54a815-7536-4104-89fd-73d7540b855e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1759d300-f0bc-47cf-8f72-0704925e74cf', NOW(), NOW(), 'Consultório de Psicologia & Família — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '2f54a815-7536-4104-89fd-73d7540b855e', 'ca7b076f-7f36-4d46-95cc-81de9e52f81b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b238e17b-d402-46e2-a3f4-1d4adacd35dc', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Castanho Taques, 110)\n**Categoria:** Psicologia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515981336622',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'b238e17b-d402-46e2-a3f4-1d4adacd35dc', '2f54a815-7536-4104-89fd-73d7540b855e', 'ca7b076f-7f36-4d46-95cc-81de9e52f81b', '1759d300-f0bc-47cf-8f72-0704925e74cf',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '27fa627b-a166-4f47-b595-44a3c0b3c05b', NOW(), NOW(), 'Clínica Médica Popular Brasilândia', 'Av. Brasil, 1150',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '75a806dc-606e-42af-b6ee-339461e5d08b', NOW(), NOW(), 'Responsável Comercial', 'Clínica Médica Popular Brasilândia',
        '551532338877', '27fa627b-a166-4f47-b595-44a3c0b3c05b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7abc4055-a2ff-4860-9e36-c89ebbc37634', NOW(), NOW(), 'Clínica Médica Popular Brasilândia — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '27fa627b-a166-4f47-b595-44a3c0b3c05b', '75a806dc-606e-42af-b6ee-339461e5d08b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ab9873f6-1e4e-4f48-89b9-e290a1015851', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1150)\n**Categoria:** Clínica Médica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532338877',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ab9873f6-1e4e-4f48-89b9-e290a1015851', '27fa627b-a166-4f47-b595-44a3c0b3c05b', '75a806dc-606e-42af-b6ee-339461e5d08b', '7abc4055-a2ff-4860-9e36-c89ebbc37634',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '77ad1320-dbbc-4e8b-9ba9-3c609de0c180', NOW(), NOW(), 'Laboratório & Coleta Brasilândia', 'R. Bartolomeu de Gusmão, 140',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5a810fac-9306-48af-bf98-9507bdeccada', NOW(), NOW(), 'Responsável Comercial', 'Laboratório & Coleta Brasilândia',
        '551532327700', '77ad1320-dbbc-4e8b-9ba9-3c609de0c180', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f199bd24-33a4-48f3-9d33-57980c154025', NOW(), NOW(), 'Laboratório & Coleta Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '77ad1320-dbbc-4e8b-9ba9-3c609de0c180', '5a810fac-9306-48af-bf98-9507bdeccada', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'efaa2baf-f34a-4b20-8249-0802c2e9f504', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Bartolomeu de Gusmão, 140)\n**Categoria:** Análises Clínicas\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532327700',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'efaa2baf-f34a-4b20-8249-0802c2e9f504', '77ad1320-dbbc-4e8b-9ba9-3c609de0c180', '5a810fac-9306-48af-bf98-9507bdeccada', 'f199bd24-33a4-48f3-9d33-57980c154025',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2f0ad3f9-330e-42b6-a64f-e3716d3e9673', NOW(), NOW(), 'Espaço Saúde & Podologia Brasil', 'R. Maciel Vaz, 310',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9fdc0c04-2c62-4352-af59-4df45721f712', NOW(), NOW(), 'Responsável Comercial', 'Espaço Saúde & Podologia Brasil',
        '5515996554411', '2f0ad3f9-330e-42b6-a64f-e3716d3e9673', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd15f3a2c-85f6-42d0-8fae-76ced47e40ed', NOW(), NOW(), 'Espaço Saúde & Podologia Brasil — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '2f0ad3f9-330e-42b6-a64f-e3716d3e9673', '9fdc0c04-2c62-4352-af59-4df45721f712', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e154a3e8-6410-47fd-bc4f-01d2a04fe4e9', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 310)\n**Categoria:** Podologia & Cuidados\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515996554411',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e154a3e8-6410-47fd-bc4f-01d2a04fe4e9', '2f0ad3f9-330e-42b6-a64f-e3716d3e9673', '9fdc0c04-2c62-4352-af59-4df45721f712', 'd15f3a2c-85f6-42d0-8fae-76ced47e40ed',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c04d1c92-23c5-41da-b575-54efdd725107', NOW(), NOW(), 'Studio Vip Brasilândia Beleza', 'Av. Brasil, 560',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c35dbd1f-240b-47cc-9ba2-cba7dfb8695e', NOW(), NOW(), 'Responsável Comercial', 'Studio Vip Brasilândia Beleza',
        '5515997331199', 'c04d1c92-23c5-41da-b575-54efdd725107', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '956bb29a-f18f-4e2a-a340-8f205205c4f4', NOW(), NOW(), 'Studio Vip Brasilândia Beleza — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'c04d1c92-23c5-41da-b575-54efdd725107', 'c35dbd1f-240b-47cc-9ba2-cba7dfb8695e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9b886967-d384-4ba7-9e60-639130db34c8', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 560)\n**Categoria:** Salão de Beleza\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997331199',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9b886967-d384-4ba7-9e60-639130db34c8', 'c04d1c92-23c5-41da-b575-54efdd725107', 'c35dbd1f-240b-47cc-9ba2-cba7dfb8695e', '956bb29a-f18f-4e2a-a340-8f205205c4f4',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '734310e3-65b5-46e0-844e-7f8104c2cbdf', NOW(), NOW(), 'Espaço Divas Cabelo & Estética', 'R. Olavo Bilac, 240',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9ae60453-eefd-499e-ba44-b914d6d621c8', NOW(), NOW(), 'Responsável Comercial', 'Espaço Divas Cabelo & Estética',
        '5515991225588', '734310e3-65b5-46e0-844e-7f8104c2cbdf', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6e8232bf-803c-49c3-bacf-72c2183f2663', NOW(), NOW(), 'Espaço Divas Cabelo & Estética — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '734310e3-65b5-46e0-844e-7f8104c2cbdf', '9ae60453-eefd-499e-ba44-b914d6d621c8', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1462c522-f24b-4c51-b91d-0d28b8a1467b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 240)\n**Categoria:** Estética & Cabelo\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515991225588',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '1462c522-f24b-4c51-b91d-0d28b8a1467b', '734310e3-65b5-46e0-844e-7f8104c2cbdf', '9ae60453-eefd-499e-ba44-b914d6d621c8', '6e8232bf-803c-49c3-bacf-72c2183f2663',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '30f527a5-688b-4a13-9de3-f7ddcedba2b3', NOW(), NOW(), 'Barbearia Tradicional Brasil', 'Av. Brasil, 890',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '38ad3d6d-3083-4cd9-a708-923152039ab2', NOW(), NOW(), 'Responsável Comercial', 'Barbearia Tradicional Brasil',
        '5515981447733', '30f527a5-688b-4a13-9de3-f7ddcedba2b3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a9ffbd14-182c-4d20-89ff-fc444cb42622', NOW(), NOW(), 'Barbearia Tradicional Brasil — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '30f527a5-688b-4a13-9de3-f7ddcedba2b3', '38ad3d6d-3083-4cd9-a708-923152039ab2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd66dacd0-1ac6-4c7c-8c33-d782ba944bed', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 890)\n**Categoria:** Barbearia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515981447733',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'd66dacd0-1ac6-4c7c-8c33-d782ba944bed', '30f527a5-688b-4a13-9de3-f7ddcedba2b3', '38ad3d6d-3083-4cd9-a708-923152039ab2', 'a9ffbd14-182c-4d20-89ff-fc444cb42622',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd4161633-1036-41e6-846b-f4e05de9347b', NOW(), NOW(), 'Salão Bela Imagem Brasilândia', 'R. Maciel Vaz, 420',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1d314a3f-eb7c-4a49-9387-17ef41725b76', NOW(), NOW(), 'Responsável Comercial', 'Salão Bela Imagem Brasilândia',
        '551532349900', 'd4161633-1036-41e6-846b-f4e05de9347b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f6947b0f-c4eb-49d0-8bfd-bd02a51a0bba', NOW(), NOW(), 'Salão Bela Imagem Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'd4161633-1036-41e6-846b-f4e05de9347b', '1d314a3f-eb7c-4a49-9387-17ef41725b76', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '110389cd-5146-4a0c-9a23-21e3d15121fb', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 420)\n**Categoria:** Cabeleireiro\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532349900',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '110389cd-5146-4a0c-9a23-21e3d15121fb', 'd4161633-1036-41e6-846b-f4e05de9347b', '1d314a3f-eb7c-4a49-9387-17ef41725b76', 'f6947b0f-c4eb-49d0-8bfd-bd02a51a0bba',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0d24cecd-f4e3-4f09-8ba6-f4b8516ad5fe', NOW(), NOW(), 'Espaço Estética & Sobrancelhas Mary', 'R. Castanho Taques, 220',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f00a2600-6c0e-4ac6-972b-a1ac34b6a1f4', NOW(), NOW(), 'Responsável Comercial', 'Espaço Estética & Sobrancelhas Mary',
        '5515996113377', '0d24cecd-f4e3-4f09-8ba6-f4b8516ad5fe', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '60959947-605a-44ca-8885-fb5c5f2c1c76', NOW(), NOW(), 'Espaço Estética & Sobrancelhas Mary — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '0d24cecd-f4e3-4f09-8ba6-f4b8516ad5fe', 'f00a2600-6c0e-4ac6-972b-a1ac34b6a1f4', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd4474bff-7a9f-4ed4-9c32-f0412f0af5d1', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Castanho Taques, 220)\n**Categoria:** Estética Facial\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515996113377',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'd4474bff-7a9f-4ed4-9c32-f0412f0af5d1', '0d24cecd-f4e3-4f09-8ba6-f4b8516ad5fe', 'f00a2600-6c0e-4ac6-972b-a1ac34b6a1f4', '60959947-605a-44ca-8885-fb5c5f2c1c76',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a4cab93c-ab0e-4299-8779-fdca4fdb686d', NOW(), NOW(), 'Barbearia Black & Gold Brasilândia', 'Av. Brasil, 1320',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8b092d8b-852d-4cb2-b338-504ba81251dc', NOW(), NOW(), 'Responsável Comercial', 'Barbearia Black & Gold Brasilândia',
        '5515997886644', 'a4cab93c-ab0e-4299-8779-fdca4fdb686d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cce70296-8fa7-40a1-99f0-5af0ea8e1efa', NOW(), NOW(), 'Barbearia Black & Gold Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'a4cab93c-ab0e-4299-8779-fdca4fdb686d', '8b092d8b-852d-4cb2-b338-504ba81251dc', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'dd72ad85-73f2-4966-8d8e-a4ca6b54459a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1320)\n**Categoria:** Barbearia Moderna\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997886644',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'dd72ad85-73f2-4966-8d8e-a4ca6b54459a', 'a4cab93c-ab0e-4299-8779-fdca4fdb686d', '8b092d8b-852d-4cb2-b338-504ba81251dc', 'cce70296-8fa7-40a1-99f0-5af0ea8e1efa',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'dcd54f8b-dbad-4951-a88a-bc7483dbe44a', NOW(), NOW(), 'Studio Nails Brasilândia Unhas', 'R. Bartolomeu de Gusmão, 80',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'df788fd6-abfd-4f47-9639-77c8edd2baab', NOW(), NOW(), 'Responsável Comercial', 'Studio Nails Brasilândia Unhas',
        '5515991669922', 'dcd54f8b-dbad-4951-a88a-bc7483dbe44a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '925b3b1f-645e-4521-b5d1-d3437bfc86df', NOW(), NOW(), 'Studio Nails Brasilândia Unhas — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'dcd54f8b-dbad-4951-a88a-bc7483dbe44a', 'df788fd6-abfd-4f47-9639-77c8edd2baab', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9d26d19b-a521-414a-a700-38d42626034d', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Bartolomeu de Gusmão, 80)\n**Categoria:** Manicure & Nails\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515991669922',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9d26d19b-a521-414a-a700-38d42626034d', 'dcd54f8b-dbad-4951-a88a-bc7483dbe44a', 'df788fd6-abfd-4f47-9639-77c8edd2baab', '925b3b1f-645e-4521-b5d1-d3437bfc86df',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5b72709c-f7b8-4afb-ae4d-8804eecd32a7', NOW(), NOW(), 'Clínica de Massoterapia & Relaxamento', 'R. Rodrigues Alves, 190',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '7a9ed3b2-aeb3-442b-add0-c5bea41773ad', NOW(), NOW(), 'Responsável Comercial', 'Clínica de Massoterapia & Relaxamento',
        '5515981224400', '5b72709c-f7b8-4afb-ae4d-8804eecd32a7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9aea42e6-3b23-4c9e-90a7-d6da3266ee4b', NOW(), NOW(), 'Clínica de Massoterapia & Relaxamento — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '5b72709c-f7b8-4afb-ae4d-8804eecd32a7', '7a9ed3b2-aeb3-442b-add0-c5bea41773ad', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '63816577-4eb8-4fb5-86cf-6fbd937a493d', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Rodrigues Alves, 190)\n**Categoria:** Massoterapia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515981224400',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '63816577-4eb8-4fb5-86cf-6fbd937a493d', '5b72709c-f7b8-4afb-ae4d-8804eecd32a7', '7a9ed3b2-aeb3-442b-add0-c5bea41773ad', '9aea42e6-3b23-4c9e-90a7-d6da3266ee4b',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '62e8e41d-3774-4b55-996f-2579700b2ea0', NOW(), NOW(), 'Auto Center Brasilândia', 'Av. Brasil, 310',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '55aad721-0d8e-46ee-a05a-53a0ff39c64b', NOW(), NOW(), 'Responsável Comercial', 'Auto Center Brasilândia',
        '551532328844', '62e8e41d-3774-4b55-996f-2579700b2ea0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '47b44509-9eb9-4a15-b1f2-ea64dfa21b6e', NOW(), NOW(), 'Auto Center Brasilândia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '62e8e41d-3774-4b55-996f-2579700b2ea0', '55aad721-0d8e-46ee-a05a-53a0ff39c64b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6c7157a5-b62e-4141-bd07-3c63f71c70e2', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 310)\n**Categoria:** Oficina Mecânica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532328844',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '6c7157a5-b62e-4141-bd07-3c63f71c70e2', '62e8e41d-3774-4b55-996f-2579700b2ea0', '55aad721-0d8e-46ee-a05a-53a0ff39c64b', '47b44509-9eb9-4a15-b1f2-ea64dfa21b6e',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '36ec18c6-3212-4b3d-93b9-40fb458f87b9', NOW(), NOW(), 'Mecânica e Injeção Sorocaba Norte', 'R. Maciel Vaz, 540',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f6ba3d87-3704-45a5-93a7-eee0252c2b05', NOW(), NOW(), 'Responsável Comercial', 'Mecânica e Injeção Sorocaba Norte',
        '551532339911', '36ec18c6-3212-4b3d-93b9-40fb458f87b9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '248f5059-90be-43c0-964f-92862f486e2f', NOW(), NOW(), 'Mecânica e Injeção Sorocaba Norte — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '36ec18c6-3212-4b3d-93b9-40fb458f87b9', 'f6ba3d87-3704-45a5-93a7-eee0252c2b05', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9ac15f89-f165-4460-8ff4-6256c6b240a8', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 540)\n**Categoria:** Injeção Eletrônica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532339911',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9ac15f89-f165-4460-8ff4-6256c6b240a8', '36ec18c6-3212-4b3d-93b9-40fb458f87b9', 'f6ba3d87-3704-45a5-93a7-eee0252c2b05', '248f5059-90be-43c0-964f-92862f486e2f',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3c89590e-2637-4419-8ed7-85c049a46268', NOW(), NOW(), 'Oficina Brasil Car Funilaria', 'Av. Brasil, 980',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e2aec947-757a-4df4-a794-4a138db18cc5', NOW(), NOW(), 'Responsável Comercial', 'Oficina Brasil Car Funilaria',
        '551532317733', '3c89590e-2637-4419-8ed7-85c049a46268', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b61660fd-6238-4ac9-9acd-42fbd8b395be', NOW(), NOW(), 'Oficina Brasil Car Funilaria — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '3c89590e-2637-4419-8ed7-85c049a46268', 'e2aec947-757a-4df4-a794-4a138db18cc5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '8857c686-84d0-4b4d-a4e6-ec225d6e02fe', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 980)\n**Categoria:** Funilaria & Pintura\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532317733',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '8857c686-84d0-4b4d-a4e6-ec225d6e02fe', '3c89590e-2637-4419-8ed7-85c049a46268', 'e2aec947-757a-4df4-a794-4a138db18cc5', 'b61660fd-6238-4ac9-9acd-42fbd8b395be',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c00c4e56-9ec5-4de4-a70d-579d3c327762', NOW(), NOW(), 'Moto Peças & Oficina Brasilândia', 'R. Olavo Bilac, 380',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a58d2be6-eda7-4463-8869-1c3a104f4157', NOW(), NOW(), 'Responsável Comercial', 'Moto Peças & Oficina Brasilândia',
        '5515997226611', 'c00c4e56-9ec5-4de4-a70d-579d3c327762', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ef24799f-1027-4c56-85b5-bd3066b5a970', NOW(), NOW(), 'Moto Peças & Oficina Brasilândia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'c00c4e56-9ec5-4de4-a70d-579d3c327762', 'a58d2be6-eda7-4463-8869-1c3a104f4157', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2afd0f7c-68b9-48ac-8440-b0617d67ee99', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 380)\n**Categoria:** Motopeças\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 5515997226611',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '2afd0f7c-68b9-48ac-8440-b0617d67ee99', 'c00c4e56-9ec5-4de4-a70d-579d3c327762', 'a58d2be6-eda7-4463-8869-1c3a104f4157', 'ef24799f-1027-4c56-85b5-bd3066b5a970',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '42b3fe0a-6c60-47e1-91b6-f231a542acbc', NOW(), NOW(), 'Pneus & Alinhamento Brasil', 'Av. Brasil, 1450',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6703220b-0491-441d-b377-28e2b95ad785', NOW(), NOW(), 'Responsável Comercial', 'Pneus & Alinhamento Brasil',
        '551532345511', '42b3fe0a-6c60-47e1-91b6-f231a542acbc', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4b385436-9dc3-440d-9734-34e271431b6d', NOW(), NOW(), 'Pneus & Alinhamento Brasil — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '42b3fe0a-6c60-47e1-91b6-f231a542acbc', '6703220b-0491-441d-b377-28e2b95ad785', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '303f05e2-ac6b-4689-b549-fbe69d5c0c1a', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1450)\n**Categoria:** Auto Center\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532345511',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '303f05e2-ac6b-4689-b549-fbe69d5c0c1a', '42b3fe0a-6c60-47e1-91b6-f231a542acbc', '6703220b-0491-441d-b377-28e2b95ad785', '4b385436-9dc3-440d-9734-34e271431b6d',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0324332f-b570-4282-9938-255dbf859628', NOW(), NOW(), 'Auto Elétrica & Baterias Brasilândia', 'R. Castanho Taques, 340',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c0757111-6776-4904-b5f1-88bd7648d194', NOW(), NOW(), 'Responsável Comercial', 'Auto Elétrica & Baterias Brasilândia',
        '5515991557788', '0324332f-b570-4282-9938-255dbf859628', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3fd4b1b8-0601-43a3-bd76-0746132d4755', NOW(), NOW(), 'Auto Elétrica & Baterias Brasilândia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '0324332f-b570-4282-9938-255dbf859628', 'c0757111-6776-4904-b5f1-88bd7648d194', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '0e1d5fc2-e63a-42a7-a3b9-d886456ad2f7', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Castanho Taques, 340)\n**Categoria:** Auto Elétrica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 5515991557788',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '0e1d5fc2-e63a-42a7-a3b9-d886456ad2f7', '0324332f-b570-4282-9938-255dbf859628', 'c0757111-6776-4904-b5f1-88bd7648d194', '3fd4b1b8-0601-43a3-bd76-0746132d4755',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '42c2d9cd-e2b2-4191-b1de-c9cb896e474b', NOW(), NOW(), 'Ar Condicionado Automotivo Norte', 'R. Bartolomeu de Gusmão, 250',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'aeeb3e90-8b14-4f2c-aae2-a6071ea5cfa1', NOW(), NOW(), 'Responsável Comercial', 'Ar Condicionado Automotivo Norte',
        '5515981338899', '42c2d9cd-e2b2-4191-b1de-c9cb896e474b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '05dd7a0c-5ba7-4745-bad9-1fd9e719ebb3', NOW(), NOW(), 'Ar Condicionado Automotivo Norte — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '42c2d9cd-e2b2-4191-b1de-c9cb896e474b', 'aeeb3e90-8b14-4f2c-aae2-a6071ea5cfa1', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9e0287b8-b9b2-43ea-97f0-6c2143704550', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Bartolomeu de Gusmão, 250)\n**Categoria:** Climatização Auto\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515981338899',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '9e0287b8-b9b2-43ea-97f0-6c2143704550', '42c2d9cd-e2b2-4191-b1de-c9cb896e474b', 'aeeb3e90-8b14-4f2c-aae2-a6071ea5cfa1', '05dd7a0c-5ba7-4745-bad9-1fd9e719ebb3',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9802bbfe-0bce-4daa-be42-293cdba74d9d', NOW(), NOW(), 'Lava Rápido & Estética Automotiva Brasil', 'Av. Brasil, 710',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ac073ef3-a0e2-4888-a59b-ab8e64358432', NOW(), NOW(), 'Responsável Comercial', 'Lava Rápido & Estética Automotiva Brasil',
        '5515996442200', '9802bbfe-0bce-4daa-be42-293cdba74d9d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd5a5fc70-1ede-4d60-8730-2bf657889efa', NOW(), NOW(), 'Lava Rápido & Estética Automotiva Brasil — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '9802bbfe-0bce-4daa-be42-293cdba74d9d', 'ac073ef3-a0e2-4888-a59b-ab8e64358432', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c5578fb1-3577-4973-b50b-821f20e0d5bb', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 710)\n**Categoria:** Estética Automotiva\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515996442200',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'c5578fb1-3577-4973-b50b-821f20e0d5bb', '9802bbfe-0bce-4daa-be42-293cdba74d9d', 'ac073ef3-a0e2-4888-a59b-ab8e64358432', 'd5a5fc70-1ede-4d60-8730-2bf657889efa',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f8811320-d5e9-4c44-a7d7-2a336a4071c9', NOW(), NOW(), 'Pet Shop Brasil & Veterinária', 'Av. Brasil, 640',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c0dc6974-fb57-497d-9dba-509fbc6c094d', NOW(), NOW(), 'Responsável Comercial', 'Pet Shop Brasil & Veterinária',
        '551532334499', 'f8811320-d5e9-4c44-a7d7-2a336a4071c9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b3e7351a-34fc-4034-ad23-43fb29a5a254', NOW(), NOW(), 'Pet Shop Brasil & Veterinária — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'f8811320-d5e9-4c44-a7d7-2a336a4071c9', 'c0dc6974-fb57-497d-9dba-509fbc6c094d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '004f7638-a1a8-4441-9fc3-e314b54f3402', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 640)\n**Categoria:** Pet Shop\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532334499',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '004f7638-a1a8-4441-9fc3-e314b54f3402', 'f8811320-d5e9-4c44-a7d7-2a336a4071c9', 'c0dc6974-fb57-497d-9dba-509fbc6c094d', 'b3e7351a-34fc-4034-ad23-43fb29a5a254',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd7fcdbbb-c4ec-4e53-806e-33f084ef514a', NOW(), NOW(), 'Agropecuária & Rações Brasilândia', 'R. Maciel Vaz, 210',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c0630811-f2b4-4b2f-a116-06ee5b0f518a', NOW(), NOW(), 'Responsável Comercial', 'Agropecuária & Rações Brasilândia',
        '551532316622', 'd7fcdbbb-c4ec-4e53-806e-33f084ef514a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6783e5e9-4431-469f-84a9-ee99fe339084', NOW(), NOW(), 'Agropecuária & Rações Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'd7fcdbbb-c4ec-4e53-806e-33f084ef514a', 'c0630811-f2b4-4b2f-a116-06ee5b0f518a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'aa04ca42-dc53-4c54-aceb-0764b4cf316b', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 210)\n**Categoria:** Agropecuária\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532316622',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'aa04ca42-dc53-4c54-aceb-0764b4cf316b', 'd7fcdbbb-c4ec-4e53-806e-33f084ef514a', 'c0630811-f2b4-4b2f-a116-06ee5b0f518a', '6783e5e9-4431-469f-84a9-ee99fe339084',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f86ffc3b-7156-4b5e-8397-0c8f8e3dfafb', NOW(), NOW(), 'Amigo Fiel Banho e Tosa', 'R. Olavo Bilac, 410',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd6bbcb99-f963-4ae7-b706-6c315f10a5cb', NOW(), NOW(), 'Responsável Comercial', 'Amigo Fiel Banho e Tosa',
        '5515997118833', 'f86ffc3b-7156-4b5e-8397-0c8f8e3dfafb', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'fc182c7e-7520-408a-97fc-382771aea716', NOW(), NOW(), 'Amigo Fiel Banho e Tosa — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'f86ffc3b-7156-4b5e-8397-0c8f8e3dfafb', 'd6bbcb99-f963-4ae7-b706-6c315f10a5cb', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b2e63508-03b0-4328-974e-c8b8af829f0c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 410)\n**Categoria:** Banho & Tosa\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515997118833',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'b2e63508-03b0-4328-974e-c8b8af829f0c', 'f86ffc3b-7156-4b5e-8397-0c8f8e3dfafb', 'd6bbcb99-f963-4ae7-b706-6c315f10a5cb', 'fc182c7e-7520-408a-97fc-382771aea716',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '33bf8acc-b9ca-41db-b30e-1af91799d037', NOW(), NOW(), 'Consultório Veterinário Brasil Animal', 'Av. Brasil, 1200',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'df8b710c-b8ac-47eb-b05b-42b947f75a63', NOW(), NOW(), 'Responsável Comercial', 'Consultório Veterinário Brasil Animal',
        '5515998335522', '33bf8acc-b9ca-41db-b30e-1af91799d037', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '843561c4-0a6d-496a-8fd5-881eb9dcbde4', NOW(), NOW(), 'Consultório Veterinário Brasil Animal — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '33bf8acc-b9ca-41db-b30e-1af91799d037', 'df8b710c-b8ac-47eb-b05b-42b947f75a63', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '5feb0cc9-206a-405a-b498-9429ed2cd8bf', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1200)\n**Categoria:** Veterinária\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 2/2\n- **Perda de Clientes Locais:** 88%\n- **Telefone:** 5515998335522',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '5feb0cc9-206a-405a-b498-9429ed2cd8bf', '33bf8acc-b9ca-41db-b30e-1af91799d037', 'df8b710c-b8ac-47eb-b05b-42b947f75a63', '843561c4-0a6d-496a-8fd5-881eb9dcbde4',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c13a76c2-31a4-467e-b771-b907eb3b4501', NOW(), NOW(), 'Padaria & Confeitaria Pão Brasil', 'Av. Brasil, 510',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6baca5a0-4893-4fa2-bda3-42e0f4a60b0f', NOW(), NOW(), 'Responsável Comercial', 'Padaria & Confeitaria Pão Brasil',
        '551532321188', 'c13a76c2-31a4-467e-b771-b907eb3b4501', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b5593bd8-bdbe-414b-83c2-8b328aa5050a', NOW(), NOW(), 'Padaria & Confeitaria Pão Brasil — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'c13a76c2-31a4-467e-b771-b907eb3b4501', '6baca5a0-4893-4fa2-bda3-42e0f4a60b0f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd4c82ab0-069b-4f2c-ab10-13b080002f50', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 510)\n**Categoria:** Padaria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532321188',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'd4c82ab0-069b-4f2c-ab10-13b080002f50', 'c13a76c2-31a4-467e-b771-b907eb3b4501', '6baca5a0-4893-4fa2-bda3-42e0f4a60b0f', 'b5593bd8-bdbe-414b-83c2-8b328aa5050a',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '59cd8df0-654d-4d8c-b153-5dd8da0e9899', NOW(), NOW(), 'Restaurante & Marmitaria Brasilândia', 'R. Maciel Vaz, 120',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '83c9376f-a275-44dc-af83-48935a030b38', NOW(), NOW(), 'Responsável Comercial', 'Restaurante & Marmitaria Brasilândia',
        '551532347744', '59cd8df0-654d-4d8c-b153-5dd8da0e9899', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'dd5e3046-34e9-4291-b8a7-6f81d6be3fd7', NOW(), NOW(), 'Restaurante & Marmitaria Brasilândia — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
        '59cd8df0-654d-4d8c-b153-5dd8da0e9899', '83c9376f-a275-44dc-af83-48935a030b38', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '118c6d96-2892-4eae-90dd-a9429597b1e8', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 120)\n**Categoria:** Restaurante\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 85%\n- **Telefone:** 551532347744',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '118c6d96-2892-4eae-90dd-a9429597b1e8', '59cd8df0-654d-4d8c-b153-5dd8da0e9899', '83c9376f-a275-44dc-af83-48935a030b38', 'dd5e3046-34e9-4291-b8a7-6f81d6be3fd7',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '611102ef-915d-4bc9-838a-1eae9b7f0759', NOW(), NOW(), 'Pizzaria Forno Nobre Brasilândia', 'Av. Brasil, 1050',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4168828c-2a42-41be-9760-c949ffc3cf02', NOW(), NOW(), 'Responsável Comercial', 'Pizzaria Forno Nobre Brasilândia',
        '551532335566', '611102ef-915d-4bc9-838a-1eae9b7f0759', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e151d6f1-c526-435b-80c1-f1d76e254f9b', NOW(), NOW(), 'Pizzaria Forno Nobre Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '611102ef-915d-4bc9-838a-1eae9b7f0759', '4168828c-2a42-41be-9760-c949ffc3cf02', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ddf43ba3-efaf-472b-b12c-6f67366281b3', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1050)\n**Categoria:** Pizzaria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532335566',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'ddf43ba3-efaf-472b-b12c-6f67366281b3', '611102ef-915d-4bc9-838a-1eae9b7f0759', '4168828c-2a42-41be-9760-c949ffc3cf02', 'e151d6f1-c526-435b-80c1-f1d76e254f9b',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '298b95a1-84d8-4877-99c6-ea0faf03784f', NOW(), NOW(), 'Pastelaria & Lanchonete do Bairro', 'R. Olavo Bilac, 180',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '38562db4-e5dd-41e2-ba5e-3e7f1aa4145f', NOW(), NOW(), 'Responsável Comercial', 'Pastelaria & Lanchonete do Bairro',
        '5515991443311', '298b95a1-84d8-4877-99c6-ea0faf03784f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f31e43f3-c457-4dbc-b785-a2a54584eb4f', NOW(), NOW(), 'Pastelaria & Lanchonete do Bairro — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '298b95a1-84d8-4877-99c6-ea0faf03784f', '38562db4-e5dd-41e2-ba5e-3e7f1aa4145f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'a96ccfde-92b0-431e-8d42-4652a6311ae6', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 180)\n**Categoria:** Lanchonete\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515991443311',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'a96ccfde-92b0-431e-8d42-4652a6311ae6', '298b95a1-84d8-4877-99c6-ea0faf03784f', '38562db4-e5dd-41e2-ba5e-3e7f1aa4145f', 'f31e43f3-c457-4dbc-b785-a2a54584eb4f',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c9999834-eac8-4126-84ff-5bfe20a9933c', NOW(), NOW(), 'Açougue & Casa de Carnes Brasil', 'Av. Brasil, 820',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '2376fef0-fb10-416c-9f97-174f8573c783', NOW(), NOW(), 'Responsável Comercial', 'Açougue & Casa de Carnes Brasil',
        '551532319944', 'c9999834-eac8-4126-84ff-5bfe20a9933c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'cd1c38e4-80ca-4202-b022-37931cf80f2d', NOW(), NOW(), 'Açougue & Casa de Carnes Brasil — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'c9999834-eac8-4126-84ff-5bfe20a9933c', '2376fef0-fb10-416c-9f97-174f8573c783', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '52721fe0-266f-44d9-9915-a9d0bf4d0b70', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 820)\n**Categoria:** Casa de Carnes\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532319944',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '52721fe0-266f-44d9-9915-a9d0bf4d0b70', 'c9999834-eac8-4126-84ff-5bfe20a9933c', '2376fef0-fb10-416c-9f97-174f8573c783', 'cd1c38e4-80ca-4202-b022-37931cf80f2d',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1b4ddb66-86a9-44a6-998b-9e794f92032e', NOW(), NOW(), 'Drogaria & Farmácia Brasilândia', 'Av. Brasil, 390',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '69f93816-de5f-4cc3-b401-6b4109d1fcb0', NOW(), NOW(), 'Responsável Comercial', 'Drogaria & Farmácia Brasilândia',
        '551532324400', '1b4ddb66-86a9-44a6-998b-9e794f92032e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '448da98d-bede-4a85-8871-d1bcaa472d9a', NOW(), NOW(), 'Drogaria & Farmácia Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '1b4ddb66-86a9-44a6-998b-9e794f92032e', '69f93816-de5f-4cc3-b401-6b4109d1fcb0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '17a88c8f-5e33-4078-946d-ad9f89534f7d', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 390)\n**Categoria:** Farmácia\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532324400',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '17a88c8f-5e33-4078-946d-ad9f89534f7d', '1b4ddb66-86a9-44a6-998b-9e794f92032e', '69f93816-de5f-4cc3-b401-6b4109d1fcb0', '448da98d-bede-4a85-8871-d1bcaa472d9a',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '4866a587-eea7-49e2-b8d5-013597913551', NOW(), NOW(), 'Marcenaria Brasil Móveis Planejados', 'R. Bartolomeu de Gusmão, 320',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ca34039f-184a-4afc-bd63-4f6c9df156e9', NOW(), NOW(), 'Responsável Comercial', 'Marcenaria Brasil Móveis Planejados',
        '5515997558811', '4866a587-eea7-49e2-b8d5-013597913551', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '88fead2d-5f9b-47cb-883e-ef58c7e3a671', NOW(), NOW(), 'Marcenaria Brasil Móveis Planejados — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '4866a587-eea7-49e2-b8d5-013597913551', 'ca34039f-184a-4afc-bd63-4f6c9df156e9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f022df0a-45ae-43de-bcfc-cd8d07b5ad44', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Bartolomeu de Gusmão, 320)\n**Categoria:** Marcenaria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 5515997558811',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'f022df0a-45ae-43de-bcfc-cd8d07b5ad44', '4866a587-eea7-49e2-b8d5-013597913551', 'ca34039f-184a-4afc-bd63-4f6c9df156e9', '88fead2d-5f9b-47cb-883e-ef58c7e3a671',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '57918154-9b2a-4070-abca-16a0e44683e8', NOW(), NOW(), 'Serralheria & Estruturas Brasilândia', 'R. Maciel Vaz, 610',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'bc5fb22e-b0ec-47e5-b53e-e0eba09915b9', NOW(), NOW(), 'Responsável Comercial', 'Serralheria & Estruturas Brasilândia',
        '5515991884422', '57918154-9b2a-4070-abca-16a0e44683e8', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'd9ed4164-6855-4010-9c26-bfb0adbe0a1f', NOW(), NOW(), 'Serralheria & Estruturas Brasilândia — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        '57918154-9b2a-4070-abca-16a0e44683e8', 'bc5fb22e-b0ec-47e5-b53e-e0eba09915b9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e9fd7a7a-1b6c-431f-9c34-9a0a09e28792', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Maciel Vaz, 610)\n**Categoria:** Serralheria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 5515991884422',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e9fd7a7a-1b6c-431f-9c34-9a0a09e28792', '57918154-9b2a-4070-abca-16a0e44683e8', 'bc5fb22e-b0ec-47e5-b53e-e0eba09915b9', 'd9ed4164-6855-4010-9c26-bfb0adbe0a1f',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c9918600-a076-45f3-b081-0e9bbe850f4c', NOW(), NOW(), 'Vidraçaria & Box Brasil Norte', 'Av. Brasil, 1280',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '6952c906-8cb1-4ee7-877a-e886c3e0b472', NOW(), NOW(), 'Responsável Comercial', 'Vidraçaria & Box Brasil Norte',
        '551532346611', 'c9918600-a076-45f3-b081-0e9bbe850f4c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1b6c058b-44cb-4b7e-afa5-dc31dbae3f7d', NOW(), NOW(), 'Vidraçaria & Box Brasil Norte — Vocação Start (Maps + Vitrine One-Page)', 'NEW', 850000000, 'BRL',
        'c9918600-a076-45f3-b081-0e9bbe850f4c', '6952c906-8cb1-4ee7-877a-e886c3e0b472', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3b4285ad-347d-4100-ab6d-a1ba335cb605', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 1280)\n**Categoria:** Vidraçaria\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 78%\n- **Telefone:** 551532346611',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '3b4285ad-347d-4100-ab6d-a1ba335cb605', 'c9918600-a076-45f3-b081-0e9bbe850f4c', '6952c906-8cb1-4ee7-877a-e886c3e0b472', '1b6c058b-44cb-4b7e-afa5-dc31dbae3f7d',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '9ac67ed8-deab-4f97-aa48-2e6f5938242f', NOW(), NOW(), 'Elétrica & Hidráulica Brasil Materiais', 'R. Castanho Taques, 450',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'b2d06694-3be6-4080-a1e3-91cf11067513', NOW(), NOW(), 'Responsável Comercial', 'Elétrica & Hidráulica Brasil Materiais',
        '551532331155', '9ac67ed8-deab-4f97-aa48-2e6f5938242f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ff73b165-256c-43b5-95d1-ca038970157c', NOW(), NOW(), 'Elétrica & Hidráulica Brasil Materiais — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '9ac67ed8-deab-4f97-aa48-2e6f5938242f', 'b2d06694-3be6-4080-a1e3-91cf11067513', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '210f22ba-9cc6-4bd8-8d5f-ee75aafa80ca', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Castanho Taques, 450)\n**Categoria:** Materiais Elétricos\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 551532331155',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '210f22ba-9cc6-4bd8-8d5f-ee75aafa80ca', '9ac67ed8-deab-4f97-aa48-2e6f5938242f', 'b2d06694-3be6-4080-a1e3-91cf11067513', 'ff73b165-256c-43b5-95d1-ca038970157c',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'f9d699e2-3582-44b2-be4b-db998e881e34', NOW(), NOW(), 'Gráfica Rápida & Comunicação Brasilândia', 'R. Olavo Bilac, 520',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'ef3fc5a0-517f-47ad-b4c9-fb17747604a0', NOW(), NOW(), 'Responsável Comercial', 'Gráfica Rápida & Comunicação Brasilândia',
        '5515996227700', 'f9d699e2-3582-44b2-be4b-db998e881e34', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3a7718d0-472a-4be4-84bb-d42973c4a456', NOW(), NOW(), 'Gráfica Rápida & Comunicação Brasilândia — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        'f9d699e2-3582-44b2-be4b-db998e881e34', 'ef3fc5a0-517f-47ad-b4c9-fb17747604a0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'e52fc769-2d39-45e0-88d6-804159e65f5c', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (R. Olavo Bilac, 520)\n**Categoria:** Gráfica\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515996227700',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), 'e52fc769-2d39-45e0-88d6-804159e65f5c', 'f9d699e2-3582-44b2-be4b-db998e881e34', 'ef3fc5a0-517f-47ad-b4c9-fb17747604a0', '3a7718d0-472a-4be4-84bb-d42973c4a456',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    

    -- Company
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
        id, "createdAt", "updatedAt", name, "addressAddressStreet1",
        "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '1bdf456a-58a5-442b-9d07-bb6fb910c1f9', NOW(), NOW(), 'Assistência Técnica de Celulares & Informática', 'Av. Brasil, 670',
        'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Person
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
        id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
        "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        'c0b1539e-d489-4d04-9ca4-90d28e007c8d', NOW(), NOW(), 'Responsável Comercial', 'Assistência Técnica de Celulares & Informática',
        '5515981552233', '1bdf456a-58a5-442b-9d07-bb6fb910c1f9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Opportunity
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
        id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
        "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '163f1fe4-424c-4f01-985d-868905dc01d3', NOW(), NOW(), 'Assistência Técnica de Celulares & Informática — Vocação Presença no Maps (Blindagem)', 'NEW', 450000000, 'BRL',
        '1bdf456a-58a5-442b-9d07-bb6fb910c1f9', 'c0b1539e-d489-4d04-9ca4-90d28e007c8d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    ) ON CONFLICT DO NOTHING;

    -- Note
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
        id, "createdAt", "updatedAt", title, "bodyV2Markdown",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        '3bffcc97-cfd9-43c5-bb88-d57b22306b24', NOW(), NOW(), 'Diagnóstico Preliminar Jev System One',
        '**Localização:** Jardim Brasilândia (Av. Brasil, 670)\n**Categoria:** Informática\n\n**Qualificação Jev:**\n- **Oferta de Melhor Fit:** Vocação Presença no Maps (Blindagem)\n- **Grau de Urgência:** 1/2\n- **Perda de Clientes Locais:** 65%\n- **Telefone:** 5515981552233',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );

    -- NoteTarget
    INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
        id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
        position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
    ) VALUES (
        gen_random_uuid(), NOW(), NOW(), '3bffcc97-cfd9-43c5-bb88-d57b22306b24', '1bdf456a-58a5-442b-9d07-bb6fb910c1f9', 'c0b1539e-d489-4d04-9ca4-90d28e007c8d', '163f1fe4-424c-4f01-985d-868905dc01d3',
        1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
    );
    