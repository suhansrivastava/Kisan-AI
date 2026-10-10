-- ==============================================================================
-- KISAN AI - SUPABASE DATABASE SCHEMA INITIALIZATION SCRIPT
-- Run this in your Supabase SQL Editor (Dashboard > SQL Editor > New query)
-- ==============================================================================

-- 1. Disease Diagnosis History Table
CREATE TABLE IF NOT EXISTS public.crop_diagnoses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    crop VARCHAR(100) NOT NULL,
    disease_name VARCHAR(255) NOT NULL,
    severity VARCHAR(50),
    confidence NUMERIC(5, 2),
    filename VARCHAR(255),
    cause TEXT,
    visual_metrics JSONB,
    symptoms JSONB,
    chemical_treatment JSONB,
    organic_treatment JSONB,
    prevention JSONB
);

-- 2. Mandi Price Rates Table
CREATE TABLE IF NOT EXISTS public.mandi_rates (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    commodity VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    variety VARCHAR(100),
    mandi VARCHAR(100) NOT NULL,
    district VARCHAR(100),
    state VARCHAR(100),
    min_price NUMERIC(10, 2),
    max_price NUMERIC(10, 2),
    modal_price NUMERIC(10, 2) NOT NULL,
    unit VARCHAR(50) DEFAULT '₹ / Quintal',
    arrival_today VARCHAR(100),
    price_change VARCHAR(50),
    trend VARCHAR(20) DEFAULT 'stable',
    msp NUMERIC(10, 2)
);

-- 3. 'Hal' AI Chat Inquiries History Table
CREATE TABLE IF NOT EXISTS public.hal_chat_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    user_message TEXT NOT NULL,
    bot_reply TEXT NOT NULL,
    language VARCHAR(10) DEFAULT 'en',
    bot_source VARCHAR(100) DEFAULT 'Hal-Builtin'
);

-- 4. Enable Row Level Security (RLS) - Permissive public access for read & insert
ALTER TABLE public.crop_diagnoses ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.mandi_rates ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.hal_chat_history ENABLE ROW LEVEL SECURITY;

-- Anonymous public read policies
CREATE POLICY "Allow public read crop_diagnoses" ON public.crop_diagnoses FOR SELECT USING (true);
CREATE POLICY "Allow public insert crop_diagnoses" ON public.crop_diagnoses FOR INSERT WITH CHECK (true);

CREATE POLICY "Allow public read mandi_rates" ON public.mandi_rates FOR SELECT USING (true);
CREATE POLICY "Allow public insert mandi_rates" ON public.mandi_rates FOR INSERT WITH CHECK (true);

CREATE POLICY "Allow public read hal_chat_history" ON public.hal_chat_history FOR SELECT USING (true);
CREATE POLICY "Allow public insert hal_chat_history" ON public.hal_chat_history FOR INSERT WITH CHECK (true);
