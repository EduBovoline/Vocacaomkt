
        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '1c39d4a6-51cb-45cf-999b-47f11a4c4367', NOW(), NOW(), 'Clínica de Psicologia & Terapias Rosália', 'R. Nicolau Alonso Filho, 88',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '8f356bc1-71de-4db9-b514-4a1fe5473513', NOW(), NOW(), 'Responsável Comercial', 'Clínica de Psicologia & Terapias Rosália',
            '5515998124010', '1c39d4a6-51cb-45cf-999b-47f11a4c4367', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '45391e5a-3dd7-42f6-a777-7030546578ce', NOW(), NOW(), 'Clínica de Psicologia & Terapias Rosália — Vocação Start', 'NEW', 850000000, 'BRL',
            '1c39d4a6-51cb-45cf-999b-47f11a4c4367', '8f356bc1-71de-4db9-b514-4a1fe5473513', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '71dda3ab-8e3d-4032-8fa5-1e0bea5ecb95', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Nicolau Alonso Filho, 88)\n**Categoria:** Psicologia\n**Canal:** WhatsApp Celular (5515998124010)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Apenas perfil em diretórios genéricos\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd9c2f0b1-2981-4867-a004-9167941121fb', NOW(), NOW(), '71dda3ab-8e3d-4032-8fa5-1e0bea5ecb95', '1c39d4a6-51cb-45cf-999b-47f11a4c4367', '8f356bc1-71de-4db9-b514-4a1fe5473513', '45391e5a-3dd7-42f6-a777-7030546578ce',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '0bf74cb8-6ec3-4be6-b3dc-ed15c7895a48', NOW(), NOW(), 'Espaço Reab Postural & RPG', 'Av. Pereira da Silva, 430',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '08a2170c-c39b-4e18-956b-ad1b110596af', NOW(), NOW(), 'Responsável Comercial', 'Espaço Reab Postural & RPG',
            '5515997812030', '0bf74cb8-6ec3-4be6-b3dc-ed15c7895a48', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '636113d0-737b-41b6-89ba-3cc5780ff177', NOW(), NOW(), 'Espaço Reab Postural & RPG — Vocação Start', 'NEW', 850000000, 'BRL',
            '0bf74cb8-6ec3-4be6-b3dc-ed15c7895a48', '08a2170c-c39b-4e18-956b-ad1b110596af', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '68b659c1-bb23-4099-abd7-c649b3967be7', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 430)\n**Categoria:** Fisioterapia\n**Canal:** WhatsApp Celular (5515997812030)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Instagram ativo sem link direto estruturado\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '81341c16-e554-4b35-a098-57a34d8a1643', NOW(), NOW(), '68b659c1-bb23-4099-abd7-c649b3967be7', '0bf74cb8-6ec3-4be6-b3dc-ed15c7895a48', '08a2170c-c39b-4e18-956b-ad1b110596af', '636113d0-737b-41b6-89ba-3cc5780ff177',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'ba161a14-0fbe-45d1-b13a-7a11f0c7bfc8', NOW(), NOW(), 'Clínica Paes Pilates & Fisio', 'Av. Pereira da Silva, 164',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'bb2e60f9-179d-4371-9454-56f8d8c2a44f', NOW(), NOW(), 'Responsável Comercial', 'Clínica Paes Pilates & Fisio',
            '5515991767971', 'ba161a14-0fbe-45d1-b13a-7a11f0c7bfc8', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '21b8c7ae-694e-4bea-9362-ab341f5f9edc', NOW(), NOW(), 'Clínica Paes Pilates & Fisio — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'ba161a14-0fbe-45d1-b13a-7a11f0c7bfc8', 'bb2e60f9-179d-4371-9454-56f8d8c2a44f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '3422b5d1-60f4-4fb3-90a1-f575e65ca875', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 164)\n**Categoria:** Pilates\n**Canal:** WhatsApp Celular (5515991767971)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Aparelhos modernos sem fotos 360 no Maps\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '24148acd-1e0b-466e-a4b4-339ba8d0f909', NOW(), NOW(), '3422b5d1-60f4-4fb3-90a1-f575e65ca875', 'ba161a14-0fbe-45d1-b13a-7a11f0c7bfc8', 'bb2e60f9-179d-4371-9454-56f8d8c2a44f', '21b8c7ae-694e-4bea-9362-ab341f5f9edc',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '99a5226d-95d7-457a-81e9-b2d47a88bc7e', NOW(), NOW(), 'Sem Limites Studio Pilates', 'R. Nicolau Alonso Filho, 215',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '1ec3f2ed-5fb6-4cdb-ba88-da218679a23b', NOW(), NOW(), 'Responsável Comercial', 'Sem Limites Studio Pilates',
            '5515997230411', '99a5226d-95d7-457a-81e9-b2d47a88bc7e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '66963a56-8a14-4ef4-a80f-1286ec3eb638', NOW(), NOW(), 'Sem Limites Studio Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            '99a5226d-95d7-457a-81e9-b2d47a88bc7e', '1ec3f2ed-5fb6-4cdb-ba88-da218679a23b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'c8fa154d-f3ee-408a-a3ff-ce5dfb8df3e1', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Nicolau Alonso Filho, 215)\n**Categoria:** Pilates\n**Canal:** WhatsApp Celular (5515997230411)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Ficha no Maps sem avaliações organizadas\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '4df90ce7-3d76-46b1-b3fb-1d91de748b67', NOW(), NOW(), 'c8fa154d-f3ee-408a-a3ff-ce5dfb8df3e1', '99a5226d-95d7-457a-81e9-b2d47a88bc7e', '1ec3f2ed-5fb6-4cdb-ba88-da218679a23b', '66963a56-8a14-4ef4-a80f-1286ec3eb638',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b7545d7e-e0ea-4e7f-86ab-0a868685b783', NOW(), NOW(), 'Pure Pilates Santa Rosália', 'R. Maria Cinto de Biaggi, 80',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd5d2965d-8780-4155-a9e8-0b6e8edf23b7', NOW(), NOW(), 'Responsável Comercial', 'Pure Pilates Santa Rosália',
            '5515998104400', 'b7545d7e-e0ea-4e7f-86ab-0a868685b783', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'ff9aa057-13f5-42dd-9f38-d5202d8372a6', NOW(), NOW(), 'Pure Pilates Santa Rosália — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'b7545d7e-e0ea-4e7f-86ab-0a868685b783', 'd5d2965d-8780-4155-a9e8-0b6e8edf23b7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '3e5668a7-2760-4979-a8b5-26957d075d91', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Maria Cinto de Biaggi, 80)\n**Categoria:** Pilates\n**Canal:** WhatsApp Celular (5515998104400)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Franquia forte, sem personalização regional\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'e56f5ec8-feb4-4253-974f-b7d214599511', NOW(), NOW(), '3e5668a7-2760-4979-a8b5-26957d075d91', 'b7545d7e-e0ea-4e7f-86ab-0a868685b783', 'd5d2965d-8780-4155-a9e8-0b6e8edf23b7', 'ff9aa057-13f5-42dd-9f38-d5202d8372a6',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'bb19a367-10db-4d20-aa96-2b6e2d70fc1a', NOW(), NOW(), 'Studio Corpo & Mente Pilates', 'R. Mascarenhas Camelo, 450',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'f932958f-190a-4434-b5bd-75632345816e', NOW(), NOW(), 'Responsável Comercial', 'Studio Corpo & Mente Pilates',
            '5515991442100', 'bb19a367-10db-4d20-aa96-2b6e2d70fc1a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '92b2b0fc-9f73-4604-ba37-37028e187055', NOW(), NOW(), 'Studio Corpo & Mente Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'bb19a367-10db-4d20-aa96-2b6e2d70fc1a', 'f932958f-190a-4434-b5bd-75632345816e', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '46400cd3-e561-4f64-a567-8a7d08effd43', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Mascarenhas Camelo, 450)\n**Categoria:** Pilates\n**Canal:** WhatsApp Celular (5515991442100)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Sem site independente, perfil no Insta com pouca bio\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '8aa35fbf-e6d8-4ea5-bde0-f37f32ad7cd3', NOW(), NOW(), '46400cd3-e561-4f64-a567-8a7d08effd43', 'bb19a367-10db-4d20-aa96-2b6e2d70fc1a', 'f932958f-190a-4434-b5bd-75632345816e', '92b2b0fc-9f73-4604-ba37-37028e187055',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b8e66c2a-a97c-4719-8f99-8714472de004', NOW(), NOW(), 'Espaço Movimento Pilates Clássico', 'Av. Pereira da Silva, 780',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '02db8785-00bc-48f6-b53c-2b72a357ee6d', NOW(), NOW(), 'Responsável Comercial', 'Espaço Movimento Pilates Clássico',
            '5515981223300', 'b8e66c2a-a97c-4719-8f99-8714472de004', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'a59b9a1e-9842-4630-bc87-e83b92a6db36', NOW(), NOW(), 'Espaço Movimento Pilates Clássico — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'b8e66c2a-a97c-4719-8f99-8714472de004', '02db8785-00bc-48f6-b53c-2b72a357ee6d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '14302d09-7442-416d-9154-9b132978e445', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 780)\n**Categoria:** Pilates\n**Canal:** WhatsApp Celular (5515981223300)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Metodologia clássica sem destaque visual no Maps\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'de3cc082-866e-40f8-b4fa-b5e7483ad246', NOW(), NOW(), '14302d09-7442-416d-9154-9b132978e445', 'b8e66c2a-a97c-4719-8f99-8714472de004', '02db8785-00bc-48f6-b53c-2b72a357ee6d', 'a59b9a1e-9842-4630-bc87-e83b92a6db36',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'a876b892-0d0c-40d0-a327-0832d973a2ea', NOW(), NOW(), 'Studio Vital Pilates & Yoga', 'R. João dos Santos, 320',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '2ecf9ff2-d63e-4839-a3c7-fa647bae7936', NOW(), NOW(), 'Responsável Comercial', 'Studio Vital Pilates & Yoga',
            '5515996551200', 'a876b892-0d0c-40d0-a327-0832d973a2ea', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '09c64479-d4eb-4766-b1d2-83cc32182b37', NOW(), NOW(), 'Studio Vital Pilates & Yoga — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'a876b892-0d0c-40d0-a327-0832d973a2ea', '2ecf9ff2-d63e-4839-a3c7-fa647bae7936', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '2fd2b62e-6f4c-4fc7-a959-1d44d58fb546', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. João dos Santos, 320)\n**Categoria:** Pilates & Yoga\n**Canal:** WhatsApp Celular (5515996551200)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Local agradável sem tour virtual no Street View\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '07177e60-43e6-4957-ae05-9463539d646e', NOW(), NOW(), '2fd2b62e-6f4c-4fc7-a959-1d44d58fb546', 'a876b892-0d0c-40d0-a327-0832d973a2ea', '2ecf9ff2-d63e-4839-a3c7-fa647bae7936', '09c64479-d4eb-4766-b1d2-83cc32182b37',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'c0e16348-f4e7-453c-810f-942d92e0615a', NOW(), NOW(), 'Instituto Postura & Movimento', 'Av. Pereira da Silva, 1420',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'a1db169f-79ee-40b3-b529-33134e370bf0', NOW(), NOW(), 'Responsável Comercial', 'Instituto Postura & Movimento',
            '5515997334411', 'c0e16348-f4e7-453c-810f-942d92e0615a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '12dca61f-5815-4ecc-8e59-b595f5b3c2ea', NOW(), NOW(), 'Instituto Postura & Movimento — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'c0e16348-f4e7-453c-810f-942d92e0615a', 'a1db169f-79ee-40b3-b529-33134e370bf0', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '687b9948-ed03-48d3-b29f-7feffd5fe9f7', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 1420)\n**Categoria:** Pilates Clínico\n**Canal:** WhatsApp Celular (5515997334411)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Falta vitrine rápida de triagem de alunos particulares\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '7f24b3a6-12fb-4fed-b34c-838e7caacb2e', NOW(), NOW(), '687b9948-ed03-48d3-b29f-7feffd5fe9f7', 'c0e16348-f4e7-453c-810f-942d92e0615a', 'a1db169f-79ee-40b3-b529-33134e370bf0', '12dca61f-5815-4ecc-8e59-b595f5b3c2ea',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '306b64a1-4482-49ae-b972-c1b02bbf9c38', NOW(), NOW(), 'Espaço Zen Terapias & Pilates', 'R. Ramos de Azevedo, 140',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '04b1a297-c026-40fb-8688-79f7f6696298', NOW(), NOW(), 'Responsável Comercial', 'Espaço Zen Terapias & Pilates',
            '5515981559944', '306b64a1-4482-49ae-b972-c1b02bbf9c38', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'fef4dc03-0637-43f3-806a-806dfc374999', NOW(), NOW(), 'Espaço Zen Terapias & Pilates — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            '306b64a1-4482-49ae-b972-c1b02bbf9c38', '04b1a297-c026-40fb-8688-79f7f6696298', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd5753e79-33c0-4f01-8528-8edb23ecacb9', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Ramos de Azevedo, 140)\n**Categoria:** Pilates & Terapias\n**Canal:** WhatsApp Celular (5515981559944)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Presença dispersa no Maps\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '0d979572-b355-4a24-80a6-8397cec6f56c', NOW(), NOW(), 'd5753e79-33c0-4f01-8528-8edb23ecacb9', '306b64a1-4482-49ae-b972-c1b02bbf9c38', '04b1a297-c026-40fb-8688-79f7f6696298', 'fef4dc03-0637-43f3-806a-806dfc374999',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b1fa7f54-b3f9-4f56-8430-a9106df9e524', NOW(), NOW(), 'Dra. Cauane Guelfi Estética Avançada', 'R. Rev. Henrique de Oliveira Camargo, 120',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '31ea46db-3f67-4fa1-833c-80cc5dd34b6b', NOW(), NOW(), 'Responsável Comercial', 'Dra. Cauane Guelfi Estética Avançada',
            '5515996411220', 'b1fa7f54-b3f9-4f56-8430-a9106df9e524', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '9392c923-0f83-4b34-a70e-f6f865347779', NOW(), NOW(), 'Dra. Cauane Guelfi Estética Avançada — Vocação Start', 'NEW', 850000000, 'BRL',
            'b1fa7f54-b3f9-4f56-8430-a9106df9e524', '31ea46db-3f67-4fa1-833c-80cc5dd34b6b', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd527b7e8-3803-4630-9f3d-4341e78ea6ae', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Rev. Henrique de Oliveira Camargo, 120)\n**Categoria:** Estética Avançada\n**Canal:** WhatsApp Celular (5515996411220)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Harmonização e tratamentos sem vitrine de autoridade\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'bdbf6402-b0d1-4e79-97cf-1b83c5b7b7b1', NOW(), NOW(), 'd527b7e8-3803-4630-9f3d-4341e78ea6ae', 'b1fa7f54-b3f9-4f56-8430-a9106df9e524', '31ea46db-3f67-4fa1-833c-80cc5dd34b6b', '9392c923-0f83-4b34-a70e-f6f865347779',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'dbe07d92-386d-4ec4-a1b7-991e8be666e6', NOW(), NOW(), 'Rô Ferreira Estética', 'Av. Pereira da Silva, 1953, Sl 4',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '465023d4-cdd5-4b8b-8c4a-b4916a6ef5c9', NOW(), NOW(), 'Responsável Comercial', 'Rô Ferreira Estética',
            '5515991166474', 'dbe07d92-386d-4ec4-a1b7-991e8be666e6', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '65556310-e8c1-4339-b2a0-d8ecad7e0eb5', NOW(), NOW(), 'Rô Ferreira Estética — Vocação Start', 'NEW', 850000000, 'BRL',
            'dbe07d92-386d-4ec4-a1b7-991e8be666e6', '465023d4-cdd5-4b8b-8c4a-b4916a6ef5c9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '0738be63-f35a-4868-a064-eded399e7682', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 1953, Sl 4)\n**Categoria:** Estética Facial\n**Canal:** WhatsApp Celular (5515991166474)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Atendimento excelente sem ficha blindada no Maps\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'df817608-e773-4c92-b3e2-629a41bad6c0', NOW(), NOW(), '0738be63-f35a-4868-a064-eded399e7682', 'dbe07d92-386d-4ec4-a1b7-991e8be666e6', '465023d4-cdd5-4b8b-8c4a-b4916a6ef5c9', '65556310-e8c1-4339-b2a0-d8ecad7e0eb5',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '6a7561c1-9c3b-485e-8857-f7242c6f5455', NOW(), NOW(), 'Espaço Bella Donna Santa Rosália', 'R. Mascarenhas Camelo, 270',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '63e2b5dd-2a9c-4984-b5b6-9ba1ed8938b5', NOW(), NOW(), 'Responsável Comercial', 'Espaço Bella Donna Santa Rosália',
            '5515997443322', '6a7561c1-9c3b-485e-8857-f7242c6f5455', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '82672e3c-3d58-4ddd-997d-865d5ecc1dd5', NOW(), NOW(), 'Espaço Bella Donna Santa Rosália — Vocação Start', 'NEW', 850000000, 'BRL',
            '6a7561c1-9c3b-485e-8857-f7242c6f5455', '63e2b5dd-2a9c-4984-b5b6-9ba1ed8938b5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '4459626b-7ef2-497a-971e-a12d5b8be0e9', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Mascarenhas Camelo, 270)\n**Categoria:** Estética Corporal\n**Canal:** WhatsApp Celular (5515997443322)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Sem site rápido mobile-first\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'fabd1f61-b364-42b4-a87f-fb9c08e21979', NOW(), NOW(), '4459626b-7ef2-497a-971e-a12d5b8be0e9', '6a7561c1-9c3b-485e-8857-f7242c6f5455', '63e2b5dd-2a9c-4984-b5b6-9ba1ed8938b5', '82672e3c-3d58-4ddd-997d-865d5ecc1dd5',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '2a08f49c-18f8-416d-9612-3586f48fe0e7', NOW(), NOW(), 'Clínica de Estética Silhouette', 'Av. Pereira da Silva, 1540',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b75d64de-0613-4f84-824d-270537c90fb5', NOW(), NOW(), 'Responsável Comercial', 'Clínica de Estética Silhouette',
            '5515996225544', '2a08f49c-18f8-416d-9612-3586f48fe0e7', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '65be158c-48ff-4215-9fc4-a048edb98ffd', NOW(), NOW(), 'Clínica de Estética Silhouette — Vocação Start', 'NEW', 850000000, 'BRL',
            '2a08f49c-18f8-416d-9612-3586f48fe0e7', 'b75d64de-0613-4f84-824d-270537c90fb5', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '52b9ef3a-2463-4ff9-b085-5a948925be2f', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 1540)\n**Categoria:** Estética Avançada\n**Canal:** WhatsApp Celular (5515996225544)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Fotos do Maps com baixa resolução\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '13303a7b-7749-4d66-8861-27c378310d34', NOW(), NOW(), '52b9ef3a-2463-4ff9-b085-5a948925be2f', '2a08f49c-18f8-416d-9612-3586f48fe0e7', 'b75d64de-0613-4f84-824d-270537c90fb5', '65be158c-48ff-4215-9fc4-a048edb98ffd',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '838cccc4-baf0-456c-86d1-b98126fc6632', NOW(), NOW(), 'Vet Care Saúde Animal', 'Av. Pereira da Silva, 68',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'f28af1bf-192f-4401-a3c6-6a962aee1eb2', NOW(), NOW(), 'Responsável Comercial', 'Vet Care Saúde Animal',
            '5515981722170', '838cccc4-baf0-456c-86d1-b98126fc6632', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '9c8ca343-83ae-42fa-bfe6-be91b41e41c2', NOW(), NOW(), 'Vet Care Saúde Animal — Vocação Start', 'NEW', 850000000, 'BRL',
            '838cccc4-baf0-456c-86d1-b98126fc6632', 'f28af1bf-192f-4401-a3c6-6a962aee1eb2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '4fec915c-b01a-46c1-b421-b340e67c0413', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 68)\n**Categoria:** Clínica Veterinária\n**Canal:** WhatsApp Celular (5515981722170)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Clínica completa sem página web rápida de plantão\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '803279a7-ea6d-45d1-b06a-2c1fb8529839', NOW(), NOW(), '4fec915c-b01a-46c1-b421-b340e67c0413', '838cccc4-baf0-456c-86d1-b98126fc6632', 'f28af1bf-192f-4401-a3c6-6a962aee1eb2', '9c8ca343-83ae-42fa-bfe6-be91b41e41c2',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd8dbac01-a83a-4656-b3d0-145006d2a267', NOW(), NOW(), 'Deniane Almeida Fisiovet', 'Av. Pereira da Silva, 68',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '1e71e9f2-bd9c-4ec5-b436-e69855e03ccd', NOW(), NOW(), 'Responsável Comercial', 'Deniane Almeida Fisiovet',
            '5515996841434', 'd8dbac01-a83a-4656-b3d0-145006d2a267', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b442c857-5a77-45d5-b686-b6a32dbb2ae7', NOW(), NOW(), 'Deniane Almeida Fisiovet — Vocação Start', 'NEW', 850000000, 'BRL',
            'd8dbac01-a83a-4656-b3d0-145006d2a267', '1e71e9f2-bd9c-4ec5-b436-e69855e03ccd', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '06840747-f49a-457a-88fc-05fb3839b124', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 68)\n**Categoria:** Reabilitação Veterinária\n**Canal:** WhatsApp Celular (5515996841434)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Nicho de altíssimo valor sem vitrine dedicada\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '7fdb8919-9039-4970-b97b-736776e4b227', NOW(), NOW(), '06840747-f49a-457a-88fc-05fb3839b124', 'd8dbac01-a83a-4656-b3d0-145006d2a267', '1e71e9f2-bd9c-4ec5-b436-e69855e03ccd', 'b442c857-5a77-45d5-b686-b6a32dbb2ae7',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '51ad331e-8d0e-4cd4-a57b-671a80391fbe', NOW(), NOW(), 'Boutique Animal Estética Pet', 'R. Nicolau Alonso Filho, 420',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'addc97c0-0925-4234-a004-1c5b83102c47', NOW(), NOW(), 'Responsável Comercial', 'Boutique Animal Estética Pet',
            '5515991332211', '51ad331e-8d0e-4cd4-a57b-671a80391fbe', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '5c90456e-0c11-4404-981d-f58f5a7ea8e3', NOW(), NOW(), 'Boutique Animal Estética Pet — Vocação Start', 'NEW', 850000000, 'BRL',
            '51ad331e-8d0e-4cd4-a57b-671a80391fbe', 'addc97c0-0925-4234-a004-1c5b83102c47', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '7aa39faa-ce44-4447-b37d-96d55624d3ed', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Nicolau Alonso Filho, 420)\n**Categoria:** Estética Pet\n**Canal:** WhatsApp Celular (5515991332211)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Atendimento carinhoso sem presença forte no Google\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Santa Rosália e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '7b4041e7-a57a-40d4-bb50-3423bd479210', NOW(), NOW(), '7aa39faa-ce44-4447-b37d-96d55624d3ed', '51ad331e-8d0e-4cd4-a57b-671a80391fbe', 'addc97c0-0925-4234-a004-1c5b83102c47', '5c90456e-0c11-4404-981d-f58f5a7ea8e3',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'aac84ab2-9591-490e-bc43-bff54f409892', NOW(), NOW(), 'Choperia & Espetaria Santa Rosália', 'Av. Pereira da Silva, 1720',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '9d19b565-cb0b-4721-97cf-eb6788b41145', NOW(), NOW(), 'Responsável Comercial', 'Choperia & Espetaria Santa Rosália',
            '5515997339900', 'aac84ab2-9591-490e-bc43-bff54f409892', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd422521b-1c38-4ebf-b297-ea1c3e6220ac', NOW(), NOW(), 'Choperia & Espetaria Santa Rosália — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            'aac84ab2-9591-490e-bc43-bff54f409892', '9d19b565-cb0b-4721-97cf-eb6788b41145', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '17aa48a4-5e5c-431f-8889-fa8f3c460075', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (Av. Pereira da Silva, 1720)\n**Categoria:** Bar & Gastronomia\n**Canal:** WhatsApp Celular (5515997339900)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 98% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Movimentado à noite sem Google Maps otimizado\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd96fa517-2372-455c-ae5a-288a6fd52716', NOW(), NOW(), '17aa48a4-5e5c-431f-8889-fa8f3c460075', 'aac84ab2-9591-490e-bc43-bff54f409892', '9d19b565-cb0b-4721-97cf-eb6788b41145', 'd422521b-1c38-4ebf-b297-ea1c3e6220ac',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '09b8e204-cfba-4f48-b774-a6864712b694', NOW(), NOW(), 'Escola de Música Notas de Ouro', 'R. Mascarenhas Camelo, 210',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '8fd2c9cb-f44d-458a-a03f-16f2f68cde2d', NOW(), NOW(), 'Responsável Comercial', 'Escola de Música Notas de Ouro',
            '5515996118833', '09b8e204-cfba-4f48-b774-a6864712b694', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '950b8698-a849-4783-90e9-345d6603dbef', NOW(), NOW(), 'Escola de Música Notas de Ouro — Combo Maps + Tour 360° GoPro Max', 'NEW', 950000000, 'BRL',
            '09b8e204-cfba-4f48-b774-a6864712b694', '8fd2c9cb-f44d-458a-a03f-16f2f68cde2d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '32107581-79d4-46f0-a619-5b5d0ee91c06', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Santa Rosália (R. Mascarenhas Camelo, 210)\n**Categoria:** Escola de Música\n**Canal:** WhatsApp Celular (5515996118833)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Combo Maps + Tour 360° GoPro Max (R$ 950.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Cursos presenciais sem vitrine de matrícula ágil\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no bairro Santa Rosália e notei algo importante: o espaço físico tem excelente apresentação, mas no Google Maps quem pesquisa na região ainda não consegue fazer um Tour Virtual 360° no Street View para conhecer a estrutura antes da visita. Posso te enviar um diagnóstico visual de 2 minutos mostrando como valorizar o espaço nas buscas? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '84388de1-83a1-476d-9f41-75104c3a80ad', NOW(), NOW(), '32107581-79d4-46f0-a619-5b5d0ee91c06', '09b8e204-cfba-4f48-b774-a6864712b694', '8fd2c9cb-f44d-458a-a03f-16f2f68cde2d', '950b8698-a849-4783-90e9-345d6603dbef',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '283a91f9-db18-424a-99db-d38fb75956a9', NOW(), NOW(), 'Clínica Dr. Marcos Dental', 'R. Maciel Vaz, 180',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '19a482de-6847-4368-9ad9-bedfd1c7ed86', NOW(), NOW(), 'Responsável Comercial', 'Clínica Dr. Marcos Dental',
            '5515997123344', '283a91f9-db18-424a-99db-d38fb75956a9', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '83ff8b99-6c25-4d33-b35b-ef22a03ec200', NOW(), NOW(), 'Clínica Dr. Marcos Dental — Vocação Start', 'NEW', 850000000, 'BRL',
            '283a91f9-db18-424a-99db-d38fb75956a9', '19a482de-6847-4368-9ad9-bedfd1c7ed86', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '33e6ccdd-7c06-429b-873c-4c96339e5a43', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Maciel Vaz, 180)\n**Categoria:** Odontologia\n**Canal:** WhatsApp Celular (5515997123344)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Ficha no Maps com fotos antigas\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'e45c47ec-5438-4187-bbf1-6e263a1ae030', NOW(), NOW(), '33e6ccdd-7c06-429b-873c-4c96339e5a43', '283a91f9-db18-424a-99db-d38fb75956a9', '19a482de-6847-4368-9ad9-bedfd1c7ed86', '83ff8b99-6c25-4d33-b35b-ef22a03ec200',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '2f1fb152-27db-4876-b318-d307dd9bd436', NOW(), NOW(), 'Dra. Camila Odontologia e Estética', 'R. Olavo Bilac, 95',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '4a097de0-e55f-435d-b22f-ee9171b7264d', NOW(), NOW(), 'Responsável Comercial', 'Dra. Camila Odontologia e Estética',
            '5515991448855', '2f1fb152-27db-4876-b318-d307dd9bd436', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '25dd7344-ca85-4aa8-8720-8b09222629ed', NOW(), NOW(), 'Dra. Camila Odontologia e Estética — Vocação Start', 'NEW', 850000000, 'BRL',
            '2f1fb152-27db-4876-b318-d307dd9bd436', '4a097de0-e55f-435d-b22f-ee9171b7264d', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'c54f9fd2-b742-4306-b878-97f863670bb1', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Olavo Bilac, 95)\n**Categoria:** Odontologia\n**Canal:** WhatsApp Celular (5515991448855)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Apenas WhatsApp de agendamento sem vitrine\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'f804d24e-1055-4772-b611-b306d6545b76', NOW(), NOW(), 'c54f9fd2-b742-4306-b878-97f863670bb1', '2f1fb152-27db-4876-b318-d307dd9bd436', '4a097de0-e55f-435d-b22f-ee9171b7264d', '25dd7344-ca85-4aa8-8720-8b09222629ed',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '15e19c83-7eab-4287-a54d-2f3e7715dac3', NOW(), NOW(), 'Consultório de Psicologia & Família', 'R. Castanho Taques, 110',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '8281a3c3-63a9-4ca1-a08f-d663d851f73a', NOW(), NOW(), 'Responsável Comercial', 'Consultório de Psicologia & Família',
            '5515981336622', '15e19c83-7eab-4287-a54d-2f3e7715dac3', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '9a67e4e1-fda7-4c66-92a4-d8c6ad304c95', NOW(), NOW(), 'Consultório de Psicologia & Família — Vocação Start', 'NEW', 850000000, 'BRL',
            '15e19c83-7eab-4287-a54d-2f3e7715dac3', '8281a3c3-63a9-4ca1-a08f-d663d851f73a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'da088a6e-64ac-4a25-8091-7f2999871916', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Castanho Taques, 110)\n**Categoria:** Psicologia\n**Canal:** WhatsApp Celular (5515981336622)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Invisível nas pesquisas do Google\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '9bb11bc2-f978-45ec-9fe1-1539bef3be3c', NOW(), NOW(), 'da088a6e-64ac-4a25-8091-7f2999871916', '15e19c83-7eab-4287-a54d-2f3e7715dac3', '8281a3c3-63a9-4ca1-a08f-d663d851f73a', '9a67e4e1-fda7-4c66-92a4-d8c6ad304c95',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '2578b16e-03e9-433f-8e95-0793fea0c71f', NOW(), NOW(), 'Espaço Divas Cabelo & Estética', 'R. Olavo Bilac, 240',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '96bfb09b-0d5b-4bcd-944e-9f1361e35d08', NOW(), NOW(), 'Responsável Comercial', 'Espaço Divas Cabelo & Estética',
            '5515991225588', '2578b16e-03e9-433f-8e95-0793fea0c71f', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '972278ea-7ee6-4509-9740-4b20579063cb', NOW(), NOW(), 'Espaço Divas Cabelo & Estética — Vocação Start', 'NEW', 850000000, 'BRL',
            '2578b16e-03e9-433f-8e95-0793fea0c71f', '96bfb09b-0d5b-4bcd-944e-9f1361e35d08', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'f7b58ef1-ac53-4246-ab75-0a2d8074c108', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Olavo Bilac, 240)\n**Categoria:** Estética & Cabelo\n**Canal:** WhatsApp Celular (5515991225588)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Fotos de trabalhos só no Instagram sem vitrine\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '3ee11ba1-602b-4bae-a9f9-88f168b42d76', NOW(), NOW(), 'f7b58ef1-ac53-4246-ab75-0a2d8074c108', '2578b16e-03e9-433f-8e95-0793fea0c71f', '96bfb09b-0d5b-4bcd-944e-9f1361e35d08', '972278ea-7ee6-4509-9740-4b20579063cb',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '72c15154-830a-4f44-8095-1b484f6e0015', NOW(), NOW(), 'Espaço Estética & Sobrancelhas Mary', 'R. Castanho Taques, 220',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '20849365-ea13-404c-9b0a-c260898f4c79', NOW(), NOW(), 'Responsável Comercial', 'Espaço Estética & Sobrancelhas Mary',
            '5515996113377', '72c15154-830a-4f44-8095-1b484f6e0015', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '946f21f9-bfb7-4427-845e-b459e2bc4398', NOW(), NOW(), 'Espaço Estética & Sobrancelhas Mary — Vocação Start', 'NEW', 850000000, 'BRL',
            '72c15154-830a-4f44-8095-1b484f6e0015', '20849365-ea13-404c-9b0a-c260898f4c79', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '5999e2ce-77eb-47df-9d50-8de55d63b87c', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Castanho Taques, 220)\n**Categoria:** Estética Facial\n**Canal:** WhatsApp Celular (5515996113377)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Depende unicamente do boca a boca\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '989249e9-d72a-4efe-b7f8-a8ec301b691c', NOW(), NOW(), '5999e2ce-77eb-47df-9d50-8de55d63b87c', '72c15154-830a-4f44-8095-1b484f6e0015', '20849365-ea13-404c-9b0a-c260898f4c79', '946f21f9-bfb7-4427-845e-b459e2bc4398',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'bfc17dc9-276c-4945-a636-f553b7cafea2', NOW(), NOW(), 'Moto Peças & Oficina Brasilândia', 'R. Olavo Bilac, 380',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'cabb18d4-05d0-4bb0-bff4-95ac25e5fe21', NOW(), NOW(), 'Responsável Comercial', 'Moto Peças & Oficina Brasilândia',
            '5515997226611', 'bfc17dc9-276c-4945-a636-f553b7cafea2', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '078712d7-e356-4ef1-bbaa-58af592b9a06', NOW(), NOW(), 'Moto Peças & Oficina Brasilândia — Vocação Start', 'NEW', 850000000, 'BRL',
            'bfc17dc9-276c-4945-a636-f553b7cafea2', 'cabb18d4-05d0-4bb0-bff4-95ac25e5fe21', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b25b3e2b-0435-468c-9f7a-f11e627adbb5', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Olavo Bilac, 380)\n**Categoria:** Motopeças\n**Canal:** WhatsApp Celular (5515997226611)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Grande movimento sem catálogo de peças online\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b036c5ad-fc38-4433-bf99-91baa00d42b8', NOW(), NOW(), 'b25b3e2b-0435-468c-9f7a-f11e627adbb5', 'bfc17dc9-276c-4945-a636-f553b7cafea2', 'cabb18d4-05d0-4bb0-bff4-95ac25e5fe21', '078712d7-e356-4ef1-bbaa-58af592b9a06',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '6c1ef1d0-5a70-4e12-b8b9-191f39d2782a', NOW(), NOW(), 'Auto Elétrica & Baterias Brasilândia', 'R. Castanho Taques, 340',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '160edd17-6eca-47cb-b18b-a3aaf475493c', NOW(), NOW(), 'Responsável Comercial', 'Auto Elétrica & Baterias Brasilândia',
            '5515991557788', '6c1ef1d0-5a70-4e12-b8b9-191f39d2782a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '18e98346-a906-45ca-a957-c9e39d7e0653', NOW(), NOW(), 'Auto Elétrica & Baterias Brasilândia — Vocação Start', 'NEW', 850000000, 'BRL',
            '6c1ef1d0-5a70-4e12-b8b9-191f39d2782a', '160edd17-6eca-47cb-b18b-a3aaf475493c', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '40bf15f5-bd51-4435-831a-05f42baf7720', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Castanho Taques, 340)\n**Categoria:** Auto Elétrica\n**Canal:** WhatsApp Celular (5515991557788)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Serviço de socorro de bateria invisível na busca móvel\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'ece90399-dd2b-42c4-b972-ed633bfd3200', NOW(), NOW(), '40bf15f5-bd51-4435-831a-05f42baf7720', '6c1ef1d0-5a70-4e12-b8b9-191f39d2782a', '160edd17-6eca-47cb-b18b-a3aaf475493c', '18e98346-a906-45ca-a957-c9e39d7e0653',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd9621157-1fec-4a2f-b7f8-4994c4f68e8a', NOW(), NOW(), 'Lava Rápido & Estética Automotiva Brasil', 'Av. Brasil, 710',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'fead0a2d-89a1-44b0-9081-a7d96725bdc6', NOW(), NOW(), 'Responsável Comercial', 'Lava Rápido & Estética Automotiva Brasil',
            '5515996442200', 'd9621157-1fec-4a2f-b7f8-4994c4f68e8a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'e7ab92e2-4103-45a3-949c-01faafc4d528', NOW(), NOW(), 'Lava Rápido & Estética Automotiva Brasil — Vocação Start', 'NEW', 850000000, 'BRL',
            'd9621157-1fec-4a2f-b7f8-4994c4f68e8a', 'fead0a2d-89a1-44b0-9081-a7d96725bdc6', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '7e214ea3-c63f-4cf3-98bb-daecfc13f30f', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (Av. Brasil, 710)\n**Categoria:** Estética Automotiva\n**Canal:** WhatsApp Celular (5515996442200)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Serviços de polimento sem fotos profissionais no Google\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'b6dbebee-05b2-4b3b-adb5-a6872ecb579f', NOW(), NOW(), '7e214ea3-c63f-4cf3-98bb-daecfc13f30f', 'd9621157-1fec-4a2f-b7f8-4994c4f68e8a', 'fead0a2d-89a1-44b0-9081-a7d96725bdc6', 'e7ab92e2-4103-45a3-949c-01faafc4d528',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'f9720d4b-e4b0-45dd-8232-a48d1c308626', NOW(), NOW(), 'Consultório Veterinário Brasil Animal', 'Av. Brasil, 1200',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '12042f1a-1d64-4428-8d30-f1749b2d4145', NOW(), NOW(), 'Responsável Comercial', 'Consultório Veterinário Brasil Animal',
            '5515998335522', 'f9720d4b-e4b0-45dd-8232-a48d1c308626', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '704cdd29-b0a9-433f-99f2-76e47cb2bccb', NOW(), NOW(), 'Consultório Veterinário Brasil Animal — Vocação Start', 'NEW', 850000000, 'BRL',
            'f9720d4b-e4b0-45dd-8232-a48d1c308626', '12042f1a-1d64-4428-8d30-f1749b2d4145', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd0543eed-651a-4cc9-825e-f0576a07158d', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (Av. Brasil, 1200)\n**Categoria:** Veterinária\n**Canal:** WhatsApp Celular (5515998335522)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Vacinas e consultas sem vitrine de atendimento\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd489232d-5d63-4d98-bde3-5fca49540e13', NOW(), NOW(), 'd0543eed-651a-4cc9-825e-f0576a07158d', 'f9720d4b-e4b0-45dd-8232-a48d1c308626', '12042f1a-1d64-4428-8d30-f1749b2d4145', '704cdd29-b0a9-433f-99f2-76e47cb2bccb',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '5223ed9c-2d70-48e8-9ee8-539201c0414a', NOW(), NOW(), 'Marcenaria Brasil Móveis Planejados', 'R. Bartolomeu de Gusmão, 320',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '026a7226-8b68-4e4d-9fd6-b94c5981cf99', NOW(), NOW(), 'Responsável Comercial', 'Marcenaria Brasil Móveis Planejados',
            '5515997558811', '5223ed9c-2d70-48e8-9ee8-539201c0414a', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'ddd39183-da8c-4f08-88c9-65204721a359', NOW(), NOW(), 'Marcenaria Brasil Móveis Planejados — Vocação Start', 'NEW', 850000000, 'BRL',
            '5223ed9c-2d70-48e8-9ee8-539201c0414a', '026a7226-8b68-4e4d-9fd6-b94c5981cf99', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd2aaa0e4-ad67-4369-8fa4-f2963b334704', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Bartolomeu de Gusmão, 320)\n**Categoria:** Marcenaria\n**Canal:** WhatsApp Celular (5515997558811)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 95% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Fábrica própria sem portfólio digital moderno\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '0520a7d6-f235-4ed8-b7b2-98155d618310', NOW(), NOW(), 'd2aaa0e4-ad67-4369-8fa4-f2963b334704', '5223ed9c-2d70-48e8-9ee8-539201c0414a', '026a7226-8b68-4e4d-9fd6-b94c5981cf99', 'ddd39183-da8c-4f08-88c9-65204721a359',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."company" (
            id, "createdAt", "updatedAt", name, "addressAddressStreet1",
            "addressAddressCity", "addressAddressState", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '51e5e5be-5641-49ec-b135-40bc82f46805', NOW(), NOW(), 'Serralheria & Estruturas Brasilândia', 'R. Maciel Vaz, 610',
            'Sorocaba', 'SP', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."person" (
            id, "createdAt", "updatedAt", "nameFirstName", "nameLastName",
            "phonesPrimaryPhoneNumber", "companyId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'd3d5fb8d-b470-45d9-8455-9256019228ea', NOW(), NOW(), 'Responsável Comercial', 'Serralheria & Estruturas Brasilândia',
            '5515991884422', '51e5e5be-5641-49ec-b135-40bc82f46805', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."opportunity" (
            id, "createdAt", "updatedAt", name, stage, "amountAmountMicros", "amountCurrencyCode",
            "companyId", "pointOfContactId", "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'c2c06c66-b6e2-474a-afa6-fe2c1a01cfe2', NOW(), NOW(), 'Serralheria & Estruturas Brasilândia — Vocação Start', 'NEW', 850000000, 'BRL',
            '51e5e5be-5641-49ec-b135-40bc82f46805', 'd3d5fb8d-b470-45d9-8455-9256019228ea', 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        ) ON CONFLICT DO NOTHING;

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."note" (
            id, "createdAt", "updatedAt", title, "bodyV2Markdown",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            'e9503931-209f-4059-97bf-64a10d821a2b', NOW(), NOW(), 'Qualificação Comercial Jev AI (Lead Ouro)', '**Bairro:** Jardim Brasilândia (R. Maciel Vaz, 610)\n**Categoria:** Serralheria\n**Canal:** WhatsApp Celular (5515991884422)\n\n**Qualificação Jev System One:**\n- **Oferta de Melhor Fit:** Vocação Start (Maps + Vitrine One-Page) (R$ 850.00)\n- **Score de Interesse Vocação:** 90% (⭐ Ouro (Alta Comissão & WhatsApp))\n- **Presença Digital:** Sem presença na internet, apenas telefone local\n\n**Hook Oficial de Abordagem:**\n> "Olá! Analisei a presença digital de vocês no Jardim Brasilândia e notei que quem pesquisa pelos seus serviços no Google encontra pouca informação institucional independente antes de chamar no WhatsApp. Posso te enviar um diagnóstico visual de 2 minutos mostrando como captar mais clientes da região? (Se preferir não receber mensagens comerciais, responda PARAR)."',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );

        INSERT INTO "workspace_2xmx8hech9nybwidia3404k2z"."noteTarget" (
            id, "createdAt", "updatedAt", "noteId", "targetCompanyId", "targetPersonId", "targetOpportunityId",
            position, "createdBySource", "createdByName", "createdByWorkspaceMemberId"
        ) VALUES (
            '95692d78-2ac7-442f-8a9a-5c8ec8d445e6', NOW(), NOW(), 'e9503931-209f-4059-97bf-64a10d821a2b', '51e5e5be-5641-49ec-b135-40bc82f46805', 'd3d5fb8d-b470-45d9-8455-9256019228ea', 'c2c06c66-b6e2-474a-afa6-fe2c1a01cfe2',
            1, 'MANUAL', 'ASSISTENTE VOCAÇÃO (JEV AI)', '1c0b8905-7e8f-4f50-90a1-6c67135bb381'
        );
        